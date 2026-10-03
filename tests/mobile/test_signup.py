from pages.mobile.base_page import MobileBasePage
import pytest
import allure
import uuid
from pages.mobile.signup_page import MobileSignupPage
from test_data.signup_cases import INVALID_CASES, get_valid_user_data

@allure.title("[모바일] 회원가입 실패: {case[tc_title]}")
@pytest.mark.parametrize("case", INVALID_CASES, ids=lambda c: c["name"])
def test_mobile_signup_invalid(mobile_driver, case):
    signup_page = MobileSignupPage(mobile_driver)
    signup_page.click_signup_link()
    
    # 기본 유효 데이터에 실패 케이스 데이터를 덮어씀
    data = get_valid_user_data(**case["override"])
    
    # 데이터가 빈 문자열이 아닌 경우에만 입력 (빈 문자열은 입력 생략하여 미입력 케이스 모사)
    if data["user_id"]: signup_page.enter_id(data["user_id"])
    if data["password"]: signup_page.enter_password(data["password"])
    if data["repassword"]: signup_page.enter_password_confirm(data["repassword"])
    if data["name"]: signup_page.enter_name(data["name"])
    if data["email"]: signup_page.enter_email(data["email"])
    
    signup_page.click_submit()
    
    # 에러 메시지 검증
    expected_msg = case["expected"]["message"]
    assert signup_page.is_error_message_displayed(expected_msg), f"에러 메시지가 노출되지 않았습니다. 예상 메시지: {expected_msg}"

@allure.id("M-TC-04")
@allure.title("[모바일] 회원가입 정상 처리 확인")
def test_mobile_signup_success(mobile_driver):
    signup_page = MobileSignupPage(mobile_driver)
    
    # [사전 조건] 회원가입 화면으로 이동
    signup_page.click_signup_link()
    
    # 임의의 새 사용자 생성
    test_id = f"test_{uuid.uuid4().hex[:5]}"
    signup_page.enter_id(test_id)
    signup_page.enter_name("모바일유저")
    signup_page.enter_email("mobile@test.com")
    signup_page.enter_password("Test1234!")
    signup_page.enter_password_confirm("Test1234!")
    
    signup_page.click_submit()
    # 로그인 화면으로 돌아왔는지 확인 로직 추가 필요
