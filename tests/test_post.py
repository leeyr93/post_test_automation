import allure
from playwright.sync_api import expect
from pages.view_page import ViewPage
from pages.post_page import PostPage
from pages.write_page import WritePage
from services import post_service
from utils import user, url
import uuid, re

@allure.id("TC-57")
@allure.title("신규 게시글 작성 후 목록 및 상세 화면 반영 확인")
def test_post_write(page, precondition_post):
    title = f"게시글 작성 제목_{uuid.uuid4().hex[:8]}"
    content = "게시글 작성 내용"

    precondition_post(title, content)
    expect(page.get_by_text(title)).to_be_visible()

    # 글 작성 확인
    post_service.open_post(page, title)
    expect(page.get_by_text(title)).to_be_visible()
    expect(page.get_by_text(content)).to_be_visible()

@allure.id("TC-58")
@allure.title("게시글 키워드로 검색 시 검색 결과 노출 확인")
def test_post_search_found(page, precondition_post):
    title = f"검색 게시글 제목_{uuid.uuid4().hex[:8]}"
    content = "검색 게시글 내용"
    precondition_post(title, content)

    # 검색 - 검색 결과가 있는 경우  
    post_service.search_post(page, title)
    expect(page.get_by_text(title)).to_be_visible()


@allure.id("TC-59")
@allure.title("존재하지 않는 키워드 검색 시 안내 문구 확인")
def test_post_search_not_found(page, precondition_post):
    board = PostPage(page)
    title = f"검색 게시글 제목_{uuid.uuid4().hex[:8]}"
    content = "검색 게시글 내용"
    precondition_post(title, content)

    # 검색 - 검색 결과가 없는 경우
    post_service.search_post(page, title + "검색 결과 없음")
    expect(board.empty_message).to_be_visible()
    expect(board.move_to_list_link).to_be_visible()

    board.click_move_to_list()
    expect(page).to_have_url(url.URL_BOARD_LIST)


@allure.id("TC-60")
@allure.title("목록 하단 페이징(다음 페이지) 클릭 시 정상 전환 확인")
def test_post_pagination(page):
    from utils.auth import login
    login(page, user.ID, user.PWD)
    board = PostPage(page)
    
    # 페이징 버튼이 있는지 확인 후 클릭
    pagination_button = page.locator(".pagination").get_by_text("2", exact=True)
    if pagination_button.is_visible():
        pagination_button.click()
        expect(page).to_have_url(re.compile(r"page=2"))


@allure.id("TC-61")
@allure.title("본인 작성 글 수정 후 상태 유지 확인")
def test_post_edit_mine(page, precondition_post):
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


@allure.id("TC-62")
@allure.title("타인이 작성한 게시글 조회 시 [수정] 버튼 미노출 확인")
def test_post_edit_others_hidden(page, precondition_post):
    view = ViewPage(page)

    title = f"수정 전 제목_{uuid.uuid4().hex[:8]}"
    content = "수정 전 내용"
    precondition_post(title, content) 

    post_service.click_post(page, user.ID_TEMP)
    expect(view.edit_button).not_to_be_visible()


@allure.id("TC-63")
@allure.title("본인 작성 글 삭제 완료 및 목록 미노출 확인")
def test_delete_post_mine(page, precondition_post):
    title = f"게시글 삭제 제목_{uuid.uuid4().hex[:8]}"
    content = "게시글 삭제 내용"
    precondition_post(title, content)

    # 내 글 삭제
    title = post_service.click_post(page, user.ID)
    post_service.delete_post(page)

    # 삭제한 글 미노출 확인
    post = PostPage(page)
    expect(post.find_post_by_title(title)).to_have_count(0)


@allure.id("TC-64")
@allure.title("타인이 작성한 게시글 조회 시 [삭제] 버튼 미노출 확인")
def test_delete_post_others_hidden(page, precondition_post):
    title = f"게시글 확인 제목_{uuid.uuid4().hex[:8]}"
    precondition_post(title, "내용")
    view = ViewPage(page)
    
    post_service.click_post(page, user.ID_TEMP)
    expect(view.delete_button).not_to_be_visible()
