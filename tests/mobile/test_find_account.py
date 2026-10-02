import pytest
import allure
from pages.mobile.find_account_page import MobileFindAccountPage

@allure.id("M-TC-05")
@allure.title("[모바일] 아이디 찾기 빈 필드 노출 확인")
def test_mobile_find_id_empty(mobile_driver):
    find_page = MobileFindAccountPage(mobile_driver)
    find_page.click_find_account_link()
    
    find_page.switch_to_find_id()
    find_page.click_find_id_button()
    
    # 폼 전송 후 노출되는 빈 필드 에러 문구 검증
    error_msg = find_page.get_error_message()
    assert "입력" in error_msg, "빈 필드 검증 에러 메시지가 표시되어야 합니다."

@allure.id("M-TC-06")
@allure.title("[모바일] 비밀번호 재설정 탭 전환 확인")
def test_mobile_find_pw_switch(mobile_driver):
    find_page = MobileFindAccountPage(mobile_driver)
    find_page.click_find_account_link()
    find_page.switch_to_reset_pw()
    
    find_page.click_verify_user_button()
