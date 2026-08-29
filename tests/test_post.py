from playwright.sync_api import expect
from pages.view_page import ViewPage
from pages.post_page import PostPage
from services import post_service
from utils import user, url
import uuid, re

#게시글 작성
def test_post_write(page, precondition_post):
    title = f"게시글 작성 제목_{uuid.uuid4().hex[:8]}"
    content = "게시글 작성 내용"

    precondition_post(title, content)
    expect(page.get_by_text(title)).to_be_visible()

    # 글 작성 확인
    post_service.open_post(page, title)
    expect(page.get_by_text(title)).to_be_visible()
    expect(page.get_by_text(content)).to_be_visible()


#게시글 검색
def test_post_search(page, precondition_post):
    board = PostPage(page)

    title = f"검색 게시글 제목_{uuid.uuid4().hex[:8]}"
    content = "검색 게시글 내용"
    precondition_post(title, content)

    # 검색 - 검색 결과가 있는 경우  
    post_service.search_post(page, title)
    expect(page.get_by_text(title)).to_be_visible()

    # 검색 - 검색 결과가 없는 경우
    post_service.search_post(page, title + "검색 결과 없음")
    expect(board.empty_message).to_be_visible()
    expect(board.move_to_list_link).to_be_visible()

    board.click_move_to_list()
    expect(page).to_have_url(url.URL_BOARD_LIST)


#게시글 수정
def test_post_edit(page, precondition_post):
    view = ViewPage(page)

    title = f"수정 전 제목_{uuid.uuid4().hex[:8]}"
    content = "수정 전 내용"
    precondition_post(title, content)

    # 글 수정
    post_service.open_post(page, title)
    new_title = f"수정 후 제목_{uuid.uuid4().hex[:8]}"
    new_content = "수정 후 내용"

    # 상세 페이지 검증
    post_service.edit_post(page, new_title, new_content)
    expect(page).to_have_url(re.compile(r"board_view/\d+"))
    expect(page.get_by_text(new_title)).to_be_visible()
    expect(page.get_by_text(new_content)).to_be_visible()

    # 게시글 목록 → 수정 내용 다시 확인
    view.click_go_main()
    post_service.open_post(page, new_title)
    expect(page.get_by_text(new_title)).to_be_visible()
    expect(page.get_by_text(new_content)).to_be_visible()

    # 남의 글 수정 불가능 확인
    view.click_go_main()
    post_service.click_post(page, user.ID_TEMP)
    expect(view.edit_button).not_to_be_visible()


#게시글 삭제
def test_delete_post(page, precondition_post):
    title = f"게시글 삭제 제목_{uuid.uuid4().hex[:8]}"
    content = "게시글 삭제 내용"
    precondition_post(title, content)

    # 내 글 삭제
    title = post_service.click_post(page, user.ID)
    post_service.delete_post(page)

    # 삭제한 글 미노출 확인
    post = PostPage(page)
    expect(post.find_post_by_title(title)).to_have_count(0)

    # 남의 글 선택 시 삭제 버튼 미노출 확인
    post_service.click_post(page, user.ID_TEMP)
    view = ViewPage(page)
    expect(view.delete_button).not_to_be_visible()


