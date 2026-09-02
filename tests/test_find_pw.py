import pytest, re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.find_pw_page import FindPwPage
from pages.reset_pw_page import ResetPwPage
from services import find_service, signup_service
from test_data.find_cases import FIND_PW_INVALID_CASES

# 1. 비밀번호 찾기 페이지 UI 기본 노출 및 placeholder 검증
def test_find_pw_page_display(page):
    find_pw_page = FindPwPage(page)
    find_pw_page.open()

    expect(find_pw_page.title).to_have_text("비밀번호 찾기")
    expect(find_pw_page.id_input).to_be_visible()
    expect(find_pw_page.id_input).to_have_attribute("placeholder", "아이디를 입력해주세요.")

    expect(find_pw_page.name_input).to_be_visible()
    expect(find_pw_page.name_input).to_have_attribute("placeholder", "이름을 입력해주세요.")

    expect(find_pw_page.email_input).to_be_visible()
    expect(find_pw_page.email_input).to_have_attribute("placeholder", "이메일을 입력해주세요.")

    expect(find_pw_page.submit_button).to_be_visible()
    expect(find_pw_page.submit_button).to_have_text("비밀번호 재설정")
    expect(find_pw_page.signup_link).to_be_visible()


# 2. 로그인 페이지에서 비밀번호 찾기 링크 클릭 이동 검증
def test_navigate_to_find_pw_from_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.click_find_pw()
    expect(page).to_have_url(re.compile(r"/find_pw$"))


# 3. 비밀번호 찾기 페이지에서 회원가입 링크 클릭 이동 검증
def test_navigate_to_join_from_find_pw(page):
    find_pw_page = FindPwPage(page)
    find_pw_page.open()
    find_pw_page.click_signup()
    expect(page).to_have_url(re.compile(r"/join$"))


# 4. 비밀번호 찾기 실패 케이스 검증 (일치 정보 없음, 미입력 등)
@pytest.mark.parametrize("case", FIND_PW_INVALID_CASES, ids=[c["name"] for c in FIND_PW_INVALID_CASES])
def test_find_pw_invalid(page, case):
    find_pw_page = FindPwPage(page)
    find_pw_page.open()

    find_pw_page.find_pw(
        user_id=case["data"]["user_id"],
        name=case["data"]["name"],
        email=case["data"]["email"]
    )
    expect(find_pw_page.server_message).to_be_visible()
    expect(find_pw_page.server_message).to_have_text(case["expected"]["message"])


# 5. 비밀번호 찾기 성공 케이스 검증 (비밀번호 재설정 화면 진입)
def test_find_pw_success(page):
    user = signup_service.register_user(page)

    reset_pw_page = find_service.find_pw(
        page,
        user_id=user["user_id"],
        name=user["name"],
        email=user["email"]
    )

    expect(reset_pw_page.title).to_have_text("비밀번호 재설정")
    expect(reset_pw_page.password_input).to_be_visible()
    expect(reset_pw_page.repassword_input).to_be_visible()
    expect(reset_pw_page.submit_button).to_be_visible()
    expect(reset_pw_page.id_hidden_input).to_have_value(user["user_id"])

