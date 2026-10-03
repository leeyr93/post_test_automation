import pytest
import allure
import uuid
from pages.mobile.login_page import MobileLoginPage
from pages.mobile.post_page import MobilePostPage
from utils import user
from utils.constants import AssertMsg
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
    assert post_page.is_post_in_list(test_title), f"{AssertMsg.POST_NOT_FOUND} (제목: {test_title})"


##TODO: 댓글 작성 기능은 text_comment.py로 이동
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
    post_page.click_more_menu()
    
    # '글 수정' 팝업 메뉴 클릭
    post_page.click_edit_post()
    
    # 내용 변경 후 저장
    new_title = test_title + " (수정됨)"
    
    # 제목 필드를 지우고 다시 입력
    post_page.clear_title()
    post_page.enter_title(new_title)
    post_page.click_edit_complete()
    
    # 목록에서 수정된 제목 확인
    assert post_page.is_post_in_list(new_title), AssertMsg.POST_NOT_FOUND

@allure.id("M-TC-64")
@allure.title("[모바일] 본인 작성 글 삭제 확인")
def test_mobile_delete_post(mobile_logged_in, mobile_test_post_title):
    mobile_driver = mobile_logged_in
    post_page = MobilePostPage(mobile_driver)
    
    # [사전 조건] 픽스처를 통해 자동 로그인 및 임시 게시글 작성됨
    test_title = mobile_test_post_title
    
    post_page.open_post_by_title(test_title)
    
    # 삭제 메뉴 클릭
    post_page.click_more_menu()
    
    post_page.click_delete_post()
    
    # 목록에서 글이 사라졌는지 확인
    # implicitly_wait 때문에 없는 요소를 찾을 때 오래 걸릴 수 있으므로 그냥 find_elements 결과가 비어있는지 체크
    assert not post_page.is_post_in_list(test_title), AssertMsg.POST_NOT_DELETED


@allure.id("M-TC-63")
@allure.title("[모바일] 타인 작성 글 수정/삭제 메뉴 미노출 확인")
def test_mobile_post_others_hidden(mobile_logged_in):
    mobile_driver = mobile_logged_in
    post_page = MobilePostPage(mobile_driver)
    
    try:
        post_page.open_post_by_title(user.ID_TEMP)
    except Exception:
        pytest.skip(f"테스트를 위한 '{user.ID_TEMP}' 작성 게시글을 화면에서 찾을 수 없어 스킵합니다.")
        
    assert not post_page.is_others_post_more_visible(), AssertMsg.AUTH_MENU_VISIBLE
