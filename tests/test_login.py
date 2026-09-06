import pytest, allure
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.post_page import PostPage
from utils.auth import login
from utils import user
import re

@allure.id("TC-21")
@allure.title("로그인 페이지 UI 확인")
def test_login_page_display(page):
    login_page = LoginPage(page)
    login_page.open()

    expect(login_page.id_input).to_be_visible()
    expect(login_page.id_input).to_have_attribute("placeholder", "아이디를 입력해주세요.")

    expect(login_page.password_input).to_be_visible()
    expect(login_page.password_input).to_have_attribute("placeholder", "비밀번호를 입력해주세요.")

    expect(login_page.login_button).to_be_visible()

@allure.id("TC-22")
@allure.title("아이디 및 비밀번호 미입력 시 에러 메시지 노출 확인")
def test_login_empty_both(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login_button.click()
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("아이디와 비밀번호를 입력해주세요")

@allure.id("TC-23")
@allure.title("아이디 미입력 시 에러 메시지 노출 확인")
def test_login_empty_id(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.password_input.fill("testpassword")
    login_page.login_button.click()
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("아이디와 비밀번호를 입력해주세요")

@allure.id("TC-24")
@allure.title("비밀번호 미입력 시 에러 메시지 노출 확인")
def test_login_empty_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.id_input.fill("test1")
    login_page.login_button.click()
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("아이디와 비밀번호를 입력해주세요")

@allure.id("TC-25")
@allure.title("미등록 계정 정보로 로그인 시도시 에러 메시지 노출 확인")
def test_login_unknown_user(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.id_input.fill("unknown_user_123")
    login_page.password_input.fill("wrongpassword123!")
    login_page.login_button.click()
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("존재하지 않는 사용자입니다.")

@allure.id("TC-26")
@allure.title("잘못된 비밀번호 입력 시 에러 메시지 노출 확인")
def test_login_wrong_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.id_input.fill(user.ID)
    login_page.password_input.fill("wrongpassword123!")
    login_page.login_button.click()
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("비밀번호가 일치하지 않습니다.")

@allure.id("TC-27")
@allure.title("로그인 완료 후 메인 화면 버튼 노출 확인")
def test_board_logged_in(page):
    login(page, user.ID, user.PWD)
    board = PostPage(page)
    expect(board.login_button).not_to_be_visible()
    expect(board.logout_button).to_be_visible()

@allure.id("TC-28")
@allure.title("로그아웃 시 메인 화면 노출 및 확인")
def test_board_logout_action(page):
    login(page, user.ID, user.PWD)
    board = PostPage(page)
    board.click_logout()
    expect(page).to_have_url(re.compile(r"/board_list$"))
    expect(board.login_button).to_be_visible()
    expect(board.logout_button).not_to_be_visible()

@allure.id("TC-29")
@allure.title("회원가입 이동 링크 확인")
def test_login_link_signup(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.click_join()
    expect(page).to_have_url(re.compile(r"/join$"))

@allure.id("TC-30")
@allure.title("아이디 찾기 이동 링크 확인")
def test_login_link_find_id(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.click_find_id()
    expect(page).to_have_url(re.compile(r"/find_id$"))

@allure.id("TC-31")
@allure.title("비밀번호 찾기 이동 링크 확인")
def test_login_link_find_pw(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.click_find_pw()
    expect(page).to_have_url(re.compile(r"/find_pw$"))
