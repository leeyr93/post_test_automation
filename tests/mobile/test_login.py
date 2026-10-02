import pytest
import allure
from pages.mobile.login_page import MobileLoginPage
from utils import user
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
    write_fab = mobile_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "글쓰기")
    assert write_fab.is_displayed(), "로그인 후 메인 화면(게시글 리스트)으로 이동하지 않았습니다."

@allure.id("M-TC-02")
@allure.title("[모바일] 빈 필드 제출 시 에러 메시지 확인")
def test_mobile_login_empty(mobile_driver):
    login_page = MobileLoginPage(mobile_driver)
    
    login_page.click_login()
    error_msg = login_page.get_error_message()
    
    assert "모두 입력해주세요" in error_msg, f"실제 에러 메시지: {error_msg}"
