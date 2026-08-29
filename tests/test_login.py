from playwright.sync_api import expect
from pages.post_page import PostPage
from pages.login_page import LoginPage
from utils.auth import login
from utils import user

# 로그인 페이지 기본 노출 확인
def test_login_page_display(page):
    login_page = LoginPage(page)
    login_page.open()

    expect(login_page.id_input).to_be_visible()
    expect(login_page.id_input).to_have_attribute("placeholder", "아이디를 입력해주세요.")

    expect(login_page.password_input).to_be_visible()
    expect(login_page.password_input).to_have_attribute("placeholder", "비밀번호를 입력해주세요.")
    
    expect(login_page.login_button).to_be_visible()


# 아이디/비밀번호 미입력 시 에러 메시지 확인
def test_login_empty_fields(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login_button.click()

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("아이디와 비밀번호를 입력해주세요")

    login_page.id_input.fill("test") 
    login_page.login_button.click()

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("아이디와 비밀번호를 입력해주세요")


# 존재하지 않는 계정으로 로그인 시 에러 메시지 확인
def test_login_unknown_user(page):
    login_page = LoginPage(page)
    login_page.open()

    not_exists_id = "test1"
    not_exists_pwd = "test1"

    login_page.id_input.fill(not_exists_id)
    login_page.password_input.fill(not_exists_pwd)

    expect(login_page.id_input).to_have_value(not_exists_id)
    expect(login_page.password_input).to_have_value(not_exists_pwd)

    login_page.login_button.click()

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("존재하지 않는 사용자입니다.")


# 로그아웃 상태 확인
def test_board_logged_out(page):
    board = PostPage(page)
    board.open()
    expect(board.login_button).to_be_visible()
    expect(board.logout_button).not_to_be_visible()


# 로그인 상태 확인
def test_board_logged_in(page):
    login(page, user.ID, user.PWD)
    board = PostPage(page)
    expect(board.login_button).not_to_be_visible()
    expect(board.logout_button).to_be_visible()