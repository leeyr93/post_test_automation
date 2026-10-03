import pytest
import allure
import uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile.post_page import MobilePostPage
from pages.mobile.login_page import MobileLoginPage
from utils import user
from utils.constants import AssertMsg

@allure.id("M-TC-67")
@allure.title("[모바일] 댓글 내용 수정 확인")
def test_mobile_edit_comment(mobile_logged_in, mobile_test_post_title):
    mobile_driver = mobile_logged_in
    post_page = MobilePostPage(mobile_driver)
    
    # [사전 조건] 자동 로그인 및 임시 게시글 작성됨
    test_title = mobile_test_post_title
    post_page.open_post_by_title(test_title)
    
    # 댓글 달기
    comment_text = f"원본 댓글 내용 {uuid.uuid4().hex[:5]}"
    post_page.enter_comment(comment_text)
    post_page.click_submit_comment()
    
    # [리팩터링] Flutter 앱에 추가된 고유 Accessibility ID(tooltip)를 사용하여 더보기 버튼 클릭
    # 앱 소스에서 tooltip: 'comment_more_btn_${comm['comm_content']}' 로 부여함
    more_btn_id = f"comment_more_btn_{comment_text}"
    mobile_driver.find_element(AppiumBy.ACCESSIBILITY_ID, more_btn_id).click()
    
    # 수정 클릭
    mobile_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "comment_menu_edit").click()
    
    # Alert 뜨면 수정 (Alert 안의 TextField)
    alert_tf = mobile_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "edit_comment_input")
    alert_tf.clear()
    edited_text = f"수정된 댓글 내용 {uuid.uuid4().hex[:5]}"
    alert_tf.send_keys(edited_text)
    
    # Alert 수정 버튼 클릭 (보통 '수정' 라벨)
    mobile_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "edit_comment_submit_btn").click()
    
    # 내용 확인
    assert post_page.is_comment_displayed(edited_text), "댓글 내용이 정상적으로 수정되지 않았습니다."


@allure.id("M-TC-68")
@allure.title("[모바일] 댓글 삭제 확인")
def test_mobile_delete_comment(mobile_logged_in, mobile_test_post_title):
    mobile_driver = mobile_logged_in
    post_page = MobilePostPage(mobile_driver)
    
    # [사전 조건] 픽스처를 통해 자동 로그인 및 임시 게시글 작성됨
    test_title = mobile_test_post_title
    
    post_page.open_post_by_title(test_title)
    
    comment_text = f"삭제될 댓글 내용 {uuid.uuid4().hex[:5]}"
    post_page.enter_comment(comment_text)
    post_page.click_submit_comment()
    
    # [리팩터링] Flutter 앱에 추가된 고유 Accessibility ID(tooltip)를 사용하여 더보기 버튼 클릭
    # 앱 소스에서 tooltip: 'comment_more_btn_${comm['comm_content']}' 로 부여함
    more_btn_id = f"comment_more_btn_{comment_text}"
    mobile_driver.find_element(AppiumBy.ACCESSIBILITY_ID, more_btn_id).click()
    
    # 삭제 클릭
    mobile_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "comment_menu_delete").click()
    
    # 삭제 확인
    WebDriverWait(mobile_driver, 10).until(EC.invisibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, f"comment_content_{comment_text}")))


@allure.id("M-TC-71")
@allure.title("[모바일] 타인 작성 댓글 수정/삭제 메뉴 미노출 확인")
def test_mobile_comment_others_hidden(mobile_driver):
    # [사전 조건] 픽스처 대신 직접 타인 계정(ID_TEMP)으로 로그인하여 글/댓글 작성
    login_page = MobileLoginPage(mobile_driver)
    post_page = MobilePostPage(mobile_driver)
    import uuid
    
    # 1. 타인 계정으로 로그인
    login_page.enter_id(user.ID_TEMP)
    login_page.enter_password(user.PWD_TEMP)
    login_page.click_login()
    
    # 2. 타인 계정으로 게시글 작성
    post_page.click_write_fab()
    test_title = f"[Mobile] 타인글 {uuid.uuid4().hex[:5]}"
    post_page.enter_title(test_title)
    post_page.enter_content("타인 계정으로 작성한 글입니다.")
    post_page.click_save_post()
    
    # 3. 해당 게시글에 들어가서 타인 계정으로 댓글 작성
    post_page.open_post_by_title(test_title)
    test_comment = f"타인 댓글 {uuid.uuid4().hex[:5]}"
    post_page.enter_comment(test_comment)
    post_page.click_submit_comment()
    
    # 4. 뒤로가기 후 로그아웃
    # Flutter 네이티브 뒤로가기 버튼(Tooltip: 'Back' -> ACCESSIBILITY_ID: 'Back')
    post_page.click_element((AppiumBy.ACCESSIBILITY_ID, "Back"))
    login_page.click_logout()
    
    # 5. 본 계정(ID_MOBILE)으로 재로그인
    login_page.enter_id(user.ID)
    login_page.enter_password(user.PWD)
    login_page.click_login()
    
    # 6. 타인이 쓴 글 찾아서 열기
    post_page.open_post_by_title(test_title)
    
    # 7. [검증] 타인의 댓글에 더보기(수정/삭제) 버튼이 노출되지 않아야 함
    assert not post_page.is_others_comment_more_visible(test_comment), AssertMsg.AUTH_MENU_VISIBLE
