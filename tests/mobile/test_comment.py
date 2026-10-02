import allure
import uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile.post_page import MobilePostPage
from utils import user

@allure.id("M-TC-67")
@allure.title("[모바일] 댓글 내용 수정 확인")
def test_mobile_edit_comment(mobile_logged_in, mobile_test_post_title):
    mobile_driver = mobile_logged_in
    post_page = MobilePostPage(mobile_driver)
    
    # [사전 조건] 픽스처를 통해 자동 로그인 및 임시 게시글 작성됨
    test_title = mobile_test_post_title
    
    post_page.open_post_by_title(test_title)
    
    # 댓글 달기
    comment_text = f"원본 댓글 내용 {uuid.uuid4().hex[:5]}"
    post_page.enter_comment(comment_text)
    post_page.click_submit_comment()
    
    # [개선] 작성한 댓글 내용을 기준으로, DOM 상에서 바로 뒤에 따라오는(following) 첫 번째 버튼을 클릭
    # [완벽 개선] 작성자(user.ID)와 댓글 내용(comment_text)이 둘 다 일치하는 영역의 더보기 버튼을 찾음
    # Flutter가 하나의 텍스트로 합쳐서 렌더링하거나, 형제 노드로 분리해서 렌더링하는 두 가지 케이스를 모두 커버하는 XPath
    more_btn_xpath = (
        f"//*[contains(@label, '{user.ID}') and contains(@label, '{comment_text}')]/following::XCUIElementTypeButton[1] | "
        f"//*[contains(@label, '{user.ID}')]/following-sibling::*[contains(@label, '{comment_text}')]/following::XCUIElementTypeButton[1] | "
        f"//*[contains(@label, '{comment_text}')]/following::XCUIElementTypeButton[1]" # Fallback
    )
    mobile_driver.find_element(AppiumBy.XPATH, more_btn_xpath).click()
    
    # 수정 클릭
    mobile_driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, '수정') or contains(@name, '수정')]").click()
    
    # Alert 뜨면 수정 (Alert 안의 TextField)
    alert_tf = mobile_driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeTextField")
    alert_tf.clear()
    edited_text = f"수정된 댓글 내용 {uuid.uuid4().hex[:5]}"
    alert_tf.send_keys(edited_text)
    
    # Alert 수정 버튼 클릭 (보통 '수정' 라벨)
    mobile_driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, '수정') or contains(@name, '수정') or contains(@label, '확인')]").click()
    
    # 내용 확인
    edited = mobile_driver.find_element(AppiumBy.XPATH, f"//*[contains(@label, '{edited_text}') or contains(@name, '{edited_text}')]")
    assert edited.is_displayed(), "댓글 내용이 정상적으로 수정되지 않았습니다."


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
    
    # [개선] 작성한 댓글 내용을 기준으로, DOM 상에서 바로 뒤에 따라오는(following) 첫 번째 버튼을 클릭
    # [완벽 개선] 작성자(user.ID)와 댓글 내용(comment_text)이 둘 다 일치하는 영역의 더보기 버튼을 찾음
    # Flutter가 하나의 텍스트로 합쳐서 렌더링하거나, 형제 노드로 분리해서 렌더링하는 두 가지 케이스를 모두 커버하는 XPath
    more_btn_xpath = (
        f"//*[contains(@label, '{user.ID}') and contains(@label, '{comment_text}')]/following::XCUIElementTypeButton[1] | "
        f"//*[contains(@label, '{user.ID}')]/following-sibling::*[contains(@label, '{comment_text}')]/following::XCUIElementTypeButton[1] | "
        f"//*[contains(@label, '{comment_text}')]/following::XCUIElementTypeButton[1]" # Fallback
    )
    mobile_driver.find_element(AppiumBy.XPATH, more_btn_xpath).click()
    
    # 삭제 클릭
    mobile_driver.find_element(AppiumBy.XPATH, "//*[contains(@label, '삭제') or contains(@name, '삭제')]").click()
    
    # 삭제 확인
    WebDriverWait(mobile_driver, 10).until(EC.invisibility_of_element_located((AppiumBy.XPATH, f"//*[contains(@label, '{comment_text}') or contains(@name, '{comment_text}')]")))

