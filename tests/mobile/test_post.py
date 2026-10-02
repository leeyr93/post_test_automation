import pytest
import allure
import uuid
from pages.mobile.login_page import MobileLoginPage
from pages.mobile.post_page import MobilePostPage
from utils import user
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.id("M-TC-07")
@allure.title("[모바일] 새 게시글 작성 및 목록 노출 확인")
def test_mobile_create_post(mobile_logged_in):
    mobile_driver = mobile_logged_in
    post_page = MobilePostPage(mobile_driver)
    
    # [사전 조건] conftest.py의 mobile_logged_in 픽스처를 통해 자동 로그인됨
    
    # 1. 게시글 작성
    post_page.click_write_fab()
    
    test_title = f"[Mobile] 테스트 제목 {uuid.uuid4().hex[:6]}"
    post_page.enter_title(test_title)
    post_page.enter_content("앱피움에서 작성된 테스트 내용입니다.")
    post_page.click_save_post()
    
    # 3. 작성 후 목록에 노출되는지 검증
    # 전역으로 설정된 암묵적 대기(implicitly_wait)를 활용하여 요소 검색
    created_post = mobile_driver.find_element(AppiumBy.XPATH, f"//*[contains(@label, '{test_title}') or contains(@name, '{test_title}')]")
    assert created_post.is_displayed(), f"작성한 게시글('{test_title}')이 목록에 노출되지 않습니다."

@allure.id("M-TC-08")
@allure.title("[모바일] 게시글 상세 진입 및 댓글 달기")
def test_mobile_write_comment(mobile_logged_in, mobile_test_post_title):
    mobile_driver = mobile_logged_in
    post_page = MobilePostPage(mobile_driver)
    
    # [사전 조건] conftest.py의 픽스처를 통해 자동 로그인 및 임시 게시글 작성됨
    test_title = mobile_test_post_title
    
    # 작성한 게시글 오픈 (동적으로 생성한 제목 이용)
    post_page.open_post_by_title(test_title)
    
    # 댓글 달기
    post_page.enter_comment("모바일 자동화로 작성한 댓글입니다.")
    post_page.click_submit_comment()

@allure.id("M-TC-62")
@allure.title("[모바일] 게시글 수정 기능 확인")
def test_mobile_edit_post(mobile_logged_in, mobile_test_post_title):
    mobile_driver = mobile_logged_in
    post_page = MobilePostPage(mobile_driver)
    
    # [사전 조건] 픽스처를 통해 자동 로그인 및 임시 게시글 작성됨
    test_title = mobile_test_post_title
    
    post_page.open_post_by_title(test_title)
    
    # 수정 메뉴 클릭
    more_btn = mobile_driver.find_elements(AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, 'Show menu') or contains(@name, 'Show menu')]")
    if not more_btn:
        # 혹시 버튼 라벨이 다를 경우 대비해 가장 첫 번째/마지막 버튼 시도
        more_btn = mobile_driver.find_elements(AppiumBy.XPATH, "//XCUIElementTypeButton")
    more_btn[-1].click()
    
    # '글 수정' 팝업 메뉴 클릭
    mobile_driver.find_element(AppiumBy.XPATH, "//*[contains(@label, '글 수정') or contains(@name, '글 수정')]").click()
    
    # 내용 변경 후 저장
    new_title = test_title + " (수정됨)"
    
    # 제목 필드를 지우고 다시 입력
    title_field = mobile_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "제목")
    title_field.clear()
    title_field.send_keys(new_title)
    mobile_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정 완료").click()
    
    # 목록에서 수정된 제목 확인
    edited = mobile_driver.find_element(AppiumBy.XPATH, f"//*[contains(@label, '{new_title}') or contains(@name, '{new_title}')]")
    assert edited.is_displayed(), "수정된 게시글 제목이 보이지 않습니다."

@allure.id("M-TC-64")
@allure.title("[모바일] 본인 작성 글 삭제 확인")
def test_mobile_delete_post(mobile_logged_in, mobile_test_post_title):
    mobile_driver = mobile_logged_in
    post_page = MobilePostPage(mobile_driver)
    
    # [사전 조건] 픽스처를 통해 자동 로그인 및 임시 게시글 작성됨
    test_title = mobile_test_post_title
    
    post_page.open_post_by_title(test_title)
    
    # 삭제 메뉴 클릭
    more_btn = mobile_driver.find_elements(AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, 'Show menu') or contains(@name, 'Show menu')]")
    if not more_btn:
        more_btn = mobile_driver.find_elements(AppiumBy.XPATH, "//XCUIElementTypeButton")
    more_btn[-1].click()
    
    mobile_driver.find_element(AppiumBy.XPATH, "//*[contains(@label, '글 삭제') or contains(@name, '글 삭제')]").click()
    
    # 목록에서 글이 사라졌는지 확인
    # implicitly_wait 때문에 없는 요소를 찾을 때 오래 걸릴 수 있으므로 그냥 find_elements 결과가 비어있는지 체크
    WebDriverWait(mobile_driver, 10).until(EC.invisibility_of_element_located((AppiumBy.XPATH, f"//*[contains(@label, '{test_title}') or contains(@name, '{test_title}')]")))

