import pytest, re, allure
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.reset_pw_page import ResetPwPage
from services import find_service, signup_service
from test_data.find_cases import RESET_PW_INVALID_CASES
from utils.auth import login
from utils import url

@allure.id("TC-56")
@allure.title("비밀번호 재설정 페이지 UI 확인")
def test_reset_pw_page_display(page):
    reset_pw_page = ResetPwPage(page)
    reset_pw_page.open()

    expect(reset_pw_page.title).to_have_text("비밀번호 재설정")
    expect(reset_pw_page.password_input).to_be_visible()
    expect(reset_pw_page.password_input).to_have_attribute("placeholder", "영문, 숫자, 특수문자 조합. 8-16자")

    expect(reset_pw_page.repassword_input).to_be_visible()
    expect(reset_pw_page.repassword_input).to_have_attribute("placeholder", "비밀번호 재입력")

    expect(reset_pw_page.submit_button).to_be_visible()
    expect(reset_pw_page.submit_button).to_have_text("확인")

@pytest.mark.parametrize("case", RESET_PW_INVALID_CASES, ids=[c["name"] for c in RESET_PW_INVALID_CASES])
def test_reset_pw_mismatch(page, case):
    allure.dynamic.id(case.get("tc_id"))
    allure.dynamic.title(case.get("tc_title"))

    user = signup_service.register_user(page)

    reset_pw_page = find_service.find_pw(
        page,
        user_id=user["user_id"],
        name=user["name"],
        email=user["email"]
    )

    reset_pw_page.reset_password(
        password=case["data"]["password"],
        repassword=case["data"]["repassword"]
    )

    expect(reset_pw_page.server_message).to_be_visible()
    expect(reset_pw_page.server_message).to_have_text(case["expected"]["message"])

@allure.id("TC-58")
@allure.title("비밀번호 재설정 확인")
def test_reset_pw_success(page):
    user = signup_service.register_user(page)
    new_password = "NewPassword123!"

    reset_pw_page = find_service.find_pw(
        page,
        user_id=user["user_id"],
        name=user["name"],
        email=user["email"]
    )
    reset_pw_page.reset_password(
        password=new_password,
        repassword=new_password
    )
    expect(page).to_have_url(re.compile(r"/login$"))

@allure.id("TC-59")
@allure.title("비밀번호 재설정 후 로그인 확인")
def test_reset_pw_login_check(page):
    user = signup_service.register_user(page)
    new_password = "NewPassword123!"

    reset_pw_page = find_service.find_pw(
        page,
        user_id=user["user_id"],
        name=user["name"],
        email=user["email"]
    )
    reset_pw_page.reset_password(
        password=new_password,
        repassword=new_password
    )
    expect(page).to_have_url(re.compile(r"/login$"))

    login_page = LoginPage(page)
    # 이전 비번 로그인 실패 확인
    login_page.login(user["user_id"], user["password"])
    expect(login_page.error_message).to_be_visible()
    
    # 새 비번 로그인 성공 확인
    login(page, user["user_id"], new_password)
    expect(page).to_have_url(url.URL_BOARD_LIST)
