import pytest
import allure
from utils import user
from utils.constants import UIErrorMsg, AssertMsg

from pages.mobile.find_account_page import MobileFindAccountPage

@allure.id("M-TC-05")
@allure.title("[모바일] 아이디 찾기 빈 필드 노출 확인")
def test_mobile_find_id_empty(mobile_driver):
    find_page = MobileFindAccountPage(mobile_driver)
    find_page.click_find_account_link()
    
    find_page.switch_to_find_id()
    find_page.click_find_id_button()
    
    # 폼 전송 후 노출되는 빈 필드 에러 문구 검증
    assert find_page.is_error_message_displayed(UIErrorMsg.FIND_ACCOUNT_EMPTY), AssertMsg.NOT_DISPLAYED

@allure.id("M-TC-06")
@allure.title("[모바일] 비밀번호 재설정 탭 전환 확인")
def test_mobile_find_pw_switch(mobile_driver):
    find_page = MobileFindAccountPage(mobile_driver)
    find_page.click_find_account_link()
    find_page.switch_to_reset_pw()
    
    find_page.click_verify_user_button()

@allure.id("M-TC-45")
@allure.title("[모바일] 올바른 정보로 아이디 찾기 성공 확인")
def test_mobile_find_id_success(mobile_driver):
    find_page = MobileFindAccountPage(mobile_driver)
    find_page.click_find_account_link()
    find_page.switch_to_find_id()
    
    find_page.enter_name("테스트유저")
    find_page.enter_email("test@example.com")
    find_page.click_find_id_button()
    
    assert find_page.is_result_displayed(user.ID), AssertMsg.FIND_ID_FAIL

import uuid
from pages.mobile.signup_page import MobileSignupPage

@allure.id("M-TC-46")
@allure.title("[모바일] 비밀번호 재설정 성공 확인")
def test_mobile_find_pw_success(mobile_driver):
    test_id = f"test{uuid.uuid4().hex[:6]}"
    test_pwd = "password123!"
    test_name = "리셋테스트"
    test_email = f"{test_id}@example.com"
    
    # 1. UI를 통한 독립적인 테스트 계정 회원가입
    signup_page = MobileSignupPage(mobile_driver)
    signup_page.click_signup_link()
    signup_page.enter_id(test_id)
    signup_page.enter_name(test_name)
    signup_page.enter_email(test_email)
    signup_page.enter_password(test_pwd)
    signup_page.enter_password_confirm(test_pwd)
    signup_page.click_submit()
    
    import time
    time.sleep(5) # 스낵바가 사라질 때까지 대기
    with open("signup_result_source.xml", "w") as f:
        f.write(mobile_driver.page_source)

    # 2. UI 테스트 진행
    find_page = MobileFindAccountPage(mobile_driver)
    find_page.click_find_account_link()
    find_page.switch_to_reset_pw()
    
    # 올바른 정보 입력 (새로 가입한 계정)
    find_page.enter_id(test_id)
    find_page.enter_name(test_name)
    find_page.enter_email(test_email)
    find_page.click_verify_user_button()
    
    time.sleep(2) # 스낵바 및 UI 변경 대기
    find_page.enter_new_password("newPassword123!")
    find_page.enter_new_password_confirm("newPassword123!")
    find_page.click_reset_pw_button()
