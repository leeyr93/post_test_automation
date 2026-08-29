from pages.post_page import PostPage
from pages.view_page import ViewPage
from services import post_service
from utils.auth import login
from utils import user
import uuid

def pre_condition_comment(page):
    board = PostPage(page)
    view = ViewPage(page)

    login(page, user.ID_TEMP, user.PWD_TEMP) # B 로그인
    title = user.ID_TEMP + f"_게시글 제목{uuid.uuid4().hex[:8]}" 
    content = user.ID_TEMP + "_게시글 내용"
    post_service.create_post(page, title, content)
    board.click_logout() # B 로그아웃

    login(page, user.ID, user.PWD) # A 로그인
    title = user.ID + f"_게시글 제목{uuid.uuid4().hex[:8]}" # A 로그인
    content = user.ID + "_게시글 내용"
    post_service.create_post(page, title, content) 

    comment_write(page, user.ID, False) # B글 - A 댓글 작성
    view.click_go_main() # 메인으로 이동하기
    board.click_logout() # A 로그아웃

    login(page, user.ID_TEMP, user.PWD_TEMP) # B 로그인
    comment_write(page, user.ID_TEMP, True) # B글 - B 댓글 작성
    view.click_go_main() # 메인으로 이동하기
    comment_write(page, user.ID_TEMP, False) # A글 - B 댓글 작성
    view.click_go_main() # 메인으로 이동하기
    board.click_logout() # B 로그아웃

    login(page, user.ID, user.PWD) # A 로그인

    return view
    

# 댓글 작성
def comment_write(page, userId=user.ID, isMyPost=True):
    post_comment = ""
    post_title, board, view = post_service.select_post(page, userId, isMyPost) # 게시글 선택

    if isMyPost:
        post_comment = userId + f"_댓글_내가 쓴 글{uuid.uuid4().hex[:8]}" 
    else:
        post_comment = userId + f"_댓글_남이 쓴 글{uuid.uuid4().hex[:8]}"

    # 댓글 입력
    view = ViewPage(page)
    view.write_comment(post_comment)
    view.click_comment() 
    
    # 작성한 댓글 확인
    view.click_go_main() # 메인으로 이동하기
    board.click_post(post_title) # 댓글 작성한 게시글 선택
    comments = page.locator("td[bgcolor='#f0f0f0']")
    target = comments.filter(has_text=post_comment)

    return target, post_comment


# 댓글 조회
def search_comment(page, userId=user.ID, isMyComment=True):
    comment = ""

    if isMyComment: # 내가 쓴 댓글
        comment = page.locator("tr").filter(
            has=page.get_by_text(userId, exact=True)
        ).first
    else: # 남이 쓴 댓글
        comment = page.locator("tr").filter(
            has_not=page.get_by_text(userId, exact=True)
        ).first

    return comment


#댓글 수정
def comment_edit(page, comment):
    new_content = f"댓글 수정{uuid.uuid4().hex[:8]}"

    # 수정 버튼 클릭 
    edit_btn = comment.locator("a:has-text('수정')")
    edit_btn.click()

    # 댓글 입력 필드 확인 및 수정
    textarea = page.locator("textarea[name='comm_content']")
    textarea.fill(new_content) 

    # 댓글수정 버튼 클릭
    page.locator("button:has-text('댓글수정')").click()

    # 수정된 댓글 확인
    updated_comment = page.locator("tr").filter(
        has=page.locator("div", has_text=new_content)
    ).first

    return updated_comment


# 댓글 삭제
def comment_delete(page, comment):
    comment_text = comment.locator("div").nth(1).inner_text().strip() # 댓글 내용 저장

    # 삭제 버튼
    delete_btn = comment.locator("a:has-text('삭제')")
    modal_id = delete_btn.get_attribute("href").replace("#", "")
    delete_btn.click()

    # 확인 클릭
    page.locator(f"#{modal_id} a:has-text('확인')").click()
    page.wait_for_load_state("networkidle")

    return comment_text


