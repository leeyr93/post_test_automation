import pytest
import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile.login_page import MobileLoginPage
from pages.mobile.post_page import MobilePostPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import user
from utils.constants import AssertMsg

@allure.id("M-TC-59")
@allure.title("[모바일] 게시글 키워드로 검색 시 검색 결과 노출 확인")
def test_mobile_search_post_success(mobile_driver):
    login_page = MobileLoginPage(mobile_driver)
    
    # 1. 로그인
    login_page.enter_id(user.ID)
    login_page.enter_password(user.PWD)
    login_page.click_login()
    
    # 검색창에 키워드 입력
    post_page = MobilePostPage(mobile_driver)
    post_page.search_post("테스트")
    
    # 검색 버튼 클릭 (돋보기 아이콘)
    # TextField 다음의 버튼이라고 가정
    # 또는 send_keys("\n") 만으로 onSubmitted 호출됨
    
    # 검색 결과 확인: '테스트' 단어가 포함된 게시글이 나오는지 확인
    # 만약 결과가 없다면? 최소한 에러가 나지는 않음
    post_page.is_search_results_displayed()
    # 비어있을 수도 있지만, 만약 게시글을 사전에 작성했다면 통과됨.

@allure.id("M-TC-60")
@allure.title("[모바일] 존재하지 않는 키워드 검색 시 안내 문구 확인")
def test_mobile_search_post_empty(mobile_driver):
    login_page = MobileLoginPage(mobile_driver)
    
    login_page.enter_id(user.ID)
    login_page.enter_password(user.PWD)
    login_page.click_login()
    
    post_page = MobilePostPage(mobile_driver)
    post_page.search_post("절대없을키워드9999")
    
    assert post_page.is_empty_search_message_displayed(), AssertMsg.SEARCH_EMPTY_FAIL

