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
