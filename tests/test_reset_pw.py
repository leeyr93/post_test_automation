import pytest, re, allure
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.reset_pw_page import ResetPwPage
from services import find_service, signup_service
from test_data.find_cases import RESET_PW_INVALID_CASES
from utils.auth import login
from utils import url


@allure.id("TC-37")
@allure.title("비밀번호 재설정 페이지 기본 요소 및 placeholder 확인")
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


@allure.id("TC-39")
@allure.title("비밀번호 재설정 후 이전 비번 실패 및 새 비번 로그인 성공 E2E 확인")
def test_find_and_reset_pw_e2e(page):
    user = signup_service.register_user(page)
    new_password = "NewPassword123!"

    # 1) 비밀번호 찾기 후 재설정 페이지 진입
    reset_pw_page = find_service.find_pw(
        page,
        user_id=user["user_id"],
        name=user["name"],
        email=user["email"]
    )

    # 2) 신규 비밀번호 입력 및 재설정 완료
    reset_pw_page.reset_password(
        password=new_password,
        repassword=new_password
    )

    # 3) 로그인 페이지로 리다이렉트 확인
    expect(page).to_have_url(re.compile(r"/login$"))

    # 4) 기존 비밀번호로 로그인 시 실패 확인
    login_page = LoginPage(page)
    login_page.login(user["user_id"], user["password"])
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("비밀번호가 일치하지 않습니다.")

    # 5) 새 비밀번호로 로그인 시 성공(게시글 목록 이동) 확인
    login(page, user["user_id"], new_password)
    expect(page).to_have_url(url.URL_BOARD_LIST)


@allure.id("TC-40")
@allure.title("재설정 URL 직접 접근(?id=xxx)을 통한 변경 및 로그인 확인")
def test_direct_reset_pw_url(page):
    user = signup_service.register_user(page)
    new_password = "DirectReset123!"

    reset_pw_page = ResetPwPage(page)
    reset_pw_page.open(user_id=user["user_id"])
    reset_pw_page.reset_password(
        password=new_password,
        repassword=new_password
    )

    expect(page).to_have_url(re.compile(r"/login$"))

    # 새 비밀번호로 로그인 확인
    login(page, user["user_id"], new_password)
    expect(page).to_have_url(url.URL_BOARD_LIST)
