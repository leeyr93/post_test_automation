import pytest, copy, allure
from playwright.sync_api import expect
from pages.signup_page import SignupPage
from test_data.signup_cases import INVALID_CASES, BASE_VALID_DATA
import uuid

def expect_error(signup_page, message):
    expect(signup_page.server_message).to_be_visible()
    expect(signup_page.server_message).to_contain_text(message)

def perform_signup(signup_page, data):
    signup_page.open()
    signup_page.signup(
        user_id=data["user_id"],
        password=data["password"],
        repassword=data["repassword"],
        name=data["name"],
        email=data["email"]
    )

def expect_placeholder(locator, text: str):
    expect(locator).to_have_attribute("placeholder", text)

@allure.id("TC-01")
@allure.title("회원가입 페이지 UI 확인")
def test_placeholders(signup):
    expect_placeholder(signup.user_id, "특수문자를 제외한 문자 조합. 1-10자")
    expect_placeholder(signup.password, "영문, 숫자, 특수문자 조합. 8-16자")
    expect_placeholder(signup.repassword, "비밀번호 재입력")
    expect_placeholder(signup.user_name, "숫자, 특수문자를 제외한 문자 조합. 1-10자")
    expect_placeholder(signup.email, "예) example@gmail.com")
    expect(signup.submit_button).to_be_visible()

@pytest.mark.parametrize("case", INVALID_CASES, ids=[c["name"] for c in INVALID_CASES])
def test_signup_invalid(signup, case):
    allure.dynamic.id(case.get("tc_id"))
    allure.dynamic.title(case.get("tc_title"))

    data = copy.deepcopy(BASE_VALID_DATA)
    data.update(case["override"])

    perform_signup(signup, data)

    expect_error(signup, case["expected"]["message"])

@allure.id("TC-22")
@allure.title("유효한 정보로 가입 성공 및 화면 이동 확인")
def test_signup_success(signup):
    data = copy.deepcopy(BASE_VALID_DATA)
    data["user_id"] = f"test1{uuid.uuid4().hex[:5]}"

    perform_signup(signup, data)
    expect(signup.page).to_have_url("http://localhost:50005/login")
