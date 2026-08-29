from playwright.sync_api import expect
from services.signup_service import perform_signup
from test_data.signup_cases import BASE_VALID_DATA, INVALID_CASES, valid_signup_case
import pytest, copy, re


def expect_error(signup_page, message):
    expect(signup_page.server_message).to_be_visible()
    expect(signup_page.server_message).to_have_text(message)


def expect_redirect(page, path):
    expect(page).to_have_url(re.compile(re.escape(path) + r"$"))


def expect_placeholder(locator, text: str):
    expect(locator).to_have_attribute("placeholder", text)


def expect_all_inputs_empty(signup_page):
    expect(signup_page.user_id).to_have_value("")
    expect(signup_page.password).to_have_value("")
    expect(signup_page.repassword).to_have_value("")
    expect(signup_page.user_name).to_have_value("")
    expect(signup_page.email).to_have_value("")


# placeholder 테스트
def test_placeholders(signup):
    expect_placeholder(signup.password, "영문, 숫자, 특수문자 조합. 8-16자")
    expect_placeholder(signup.repassword, "비밀번호 재입력")
    expect_placeholder(signup.user_name, "숫자, 특수문자를 제외한 문자 조합. 1-10자")
    expect_placeholder(signup.email, "예) example@gmail.com")


# invalid 케이스
@pytest.mark.parametrize("case", INVALID_CASES, ids=[c["name"] for c in INVALID_CASES])
def test_signup_invalid(signup, case):
    data = copy.deepcopy(BASE_VALID_DATA)
    data.update(case["override"])

    perform_signup(signup, data)

    expect_error(signup, case["expected"]["message"])

    if case["expected"].get("reset"):
        expect_all_inputs_empty(signup)


# 성공 케이스
@pytest.mark.parametrize("case", [valid_signup_case()])
def test_signup_success(signup, case):
    perform_signup(signup, case["data"])
    expect_redirect(signup.page, case["expected"]["redirect"])
