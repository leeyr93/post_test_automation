from pages.post_page import PostPage
from pages.write_page import WritePage
from pages.view_page import ViewPage
from utils import user


#게시글 검색
def search_post(page, keyword):
    board = PostPage(page)
    board.search(keyword)

    if board.post_rows.count() > 0:
        return "FOUND"
    else:
        return "NOT_FOUND"


#게시글 작성
def create_post(page, title, content):
    board = PostPage(page)
    board.click_write()

    write = WritePage(page)
    write.write_post(title, content)
    write.submit_post()


#게시글 선택 (사용자 기준)
def click_post(page, user_id):
    board = PostPage(page)
    row = board.find_post_by_writer(user_id)

    if not row:
        raise Exception("작성한 게시글 없음")

    title = row.locator("td").nth(1).inner_text().strip()
    row.click()
    return title


#게시글 선택 (제목 기준)
def open_post(page, title):
    board = PostPage(page)
    board.click_post(title)


#게시글 수정
def edit_post(page, new_title, new_content):
    view = ViewPage(page)
    view.click_edit()

    write = WritePage(page)
    write.write_post(new_title, new_content)
    write.submit_post()


#게시글 삭제
def delete_post(page):
    post = PostPage(page)
    view = ViewPage(page)

    view.click_delete()
    post.delete_modal_wait_visible()
    post.delete_confirm()


#게시글 선택
def select_post(page, userId, isMyPost):
    post_title = ""
    board = PostPage(page)
    view = ViewPage(page)
    
    if isMyPost: # 본인이 작성한 글
        post_title = click_post(page, userId) # 내가 작성한 글 선택
    else: # 본인이 작성하지 않은 글
        if userId == user.ID :
            post_title = click_post(page, user.ID_TEMP) # 내가 작성하지 않은 글 선택 (dbfks > dbfks3 선택)
        else:
            post_title = click_post(page, user.ID) # 내가 작성하지 않은 글 선택 (dbfks3 > dbfks 선택)

    return post_title, board, view