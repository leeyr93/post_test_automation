import pytest
import allure
import uuid
from pages.mobile.signup_page import MobileSignupPage

@allure.id("M-TC-03")
@allure.title("[모바일] 회원가입 빈 필드 에러 노출 확인")
def test_mobile_signup_empty(mobile_driver):
    signup_page = MobileSignupPage(mobile_driver)
    signup_page.click_signup_link()
    
    signup_page.click_submit()
    error_msg = signup_page.get_error_message()
    
    assert "입력해주세요" in error_msg, "빈 필드 검증 에러 메시지가 표시되어야 합니다."

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
