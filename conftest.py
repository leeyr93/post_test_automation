import pytest, uuid
from playwright.sync_api import sync_playwright
from services import post_service
from pages.signup_page import SignupPage
from utils.auth import login
from utils import user

@pytest.fixture(scope="session")
def browser():
    """
    테스트 세션 전체에서 하나의 브라우저만 사용
    → 테스트 속도 개선
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """
    각 테스트마다 새로운 브라우저 컨텍스트 제공
    → 테스트 간 상태 격리 (쿠키/세션 충돌 방지)
    """
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def signup(page):
    signup_page = SignupPage(page)
    signup_page.open()
    return signup_page


# 사전 조건 - 로그인 및 게시글 작성
@pytest.fixture
def precondition_post(page):
    created_titles = []  # 테스트에서 작성한 게시글 title 목록

    def _create(title=None, content=None):
        if title is None and content is None:
            title = user.ID + f"_게시글 제목_{uuid.uuid4().hex[:8]}"
            content = user.ID + "_게시글 내용"

        login(page, user.ID, user.PWD)
        post_service.create_post(page, title, content)
        created_titles.append(title)

    yield _create

    # teardown: 테스트에서 작성한 게시글 전부 삭제 (수정한 게시글 제외)
    for title in created_titles:
        try:
            post_service.open_post(page, title)
            post_service.delete_post(page)
        except Exception as e:
            print(f"[teardown 실패] '{title}' 삭제 안 됨: {e}")