import pytest
import allure
from pages.mobile.login_page import MobileLoginPage
from utils import user
from utils.constants import UIErrorMsg, AssertMsg
from appium.webdriver.common.appiumby import AppiumBy

@allure.id("M-TC-01")
@allure.title("[모바일] 올바른 계정으로 로그인 성공 확인")
def test_mobile_login_success(mobile_driver):
    """
    모바일 전용 로그인 성공 테스트
    - mobile_driver 픽스처는 tests/mobile/conftest.py 에서 로드됨 (웹 브라우저와 격리)
    """
    login_page = MobileLoginPage(mobile_driver)
    
    # 공용 유틸리티(user) 재사용
    login_page.enter_id(user.ID)
    login_page.enter_password(user.PWD)
    login_page.click_login()
    
    # 모바일 게시판 메인 화면(게시글 리스트) 진입 여부 검증 (글쓰기 FAB 노출 확인)
    from pages.mobile.post_page import MobilePostPage
    assert MobilePostPage(mobile_driver).is_displayed((AppiumBy.ACCESSIBILITY_ID, "글쓰기"), timeout=15), AssertMsg.LOGIN_SUCCESS_FAIL

@allure.id("M-TC-02")
@allure.title("[모바일] 빈 필드 제출 시 에러 메시지 확인")
def test_mobile_login_empty_both(mobile_driver):
    login_page = MobileLoginPage(mobile_driver)
    login_page.click_login()
    assert login_page.is_error_message_displayed(UIErrorMsg.LOGIN_EMPTY_BOTH), AssertMsg.NOT_DISPLAYED

@allure.id("M-TC-24")
@allure.title("[모바일] 아이디 미입력 시 에러 메시지 노출 확인")
def test_mobile_login_empty_id(mobile_driver):
    login_page = MobileLoginPage(mobile_driver)
    login_page.enter_password("testpassword")
    login_page.click_login()
    assert login_page.is_error_message_displayed(UIErrorMsg.LOGIN_EMPTY_ID), AssertMsg.NOT_DISPLAYED

@allure.id("M-TC-25")
@allure.title("[모바일] 비밀번호 미입력 시 에러 메시지 노출 확인")
def test_mobile_login_empty_password(mobile_driver):
    login_page = MobileLoginPage(mobile_driver)
    login_page.enter_id("testuser")
    login_page.click_login()
    assert login_page.is_error_message_displayed(UIErrorMsg.LOGIN_EMPTY_PASSWORD), AssertMsg.NOT_DISPLAYED

@allure.id("M-TC-29")
@allure.title("[모바일] 로그아웃 시 메인 화면(로그인 화면) 노출 확인")
def test_mobile_logout_action(mobile_driver):
    login_page = MobileLoginPage(mobile_driver)
    
    login_page.enter_id(user.ID)
    login_page.enter_password(user.PWD)
    login_page.click_login()
    
    # 로그인 완료 후 FAB 대기 
    from pages.mobile.post_page import MobilePostPage
    assert MobilePostPage(mobile_driver).is_displayed((AppiumBy.ACCESSIBILITY_ID, "글쓰기"), timeout=15)
    
    login_page.click_logout()
    assert login_page.is_login_screen_displayed(), AssertMsg.LOGOUT_FAIL

@allure.id("M-TC-26")
@allure.title("[모바일] 미등록 계정 정보로 로그인 시도시 에러 메시지 노출 확인")
def test_mobile_login_unknown_user(mobile_driver):
    login_page = MobileLoginPage(mobile_driver)
    
    login_page.enter_id("unknown_user_123")
    login_page.enter_password("wrongpassword123!")
    login_page.click_login()
    
    assert login_page.is_error_message_displayed(UIErrorMsg.LOGIN_UNKNOWN_USER), AssertMsg.ERROR_MISMATCH

@allure.id("M-TC-27")
@allure.title("[모바일] 잘못된 비밀번호 입력 시 에러 메시지 노출 확인")
def test_mobile_login_wrong_password(mobile_driver):
    login_page = MobileLoginPage(mobile_driver)
    
    login_page.enter_id(user.ID)
    login_page.enter_password("wrongpassword123!")
    login_page.click_login()
    
    assert login_page.is_error_message_displayed(UIErrorMsg.LOGIN_WRONG_PASSWORD), AssertMsg.ERROR_MISMATCH
