import pytest, uuid
from appium import webdriver
from appium.options.ios import XCUITestOptions
from pages.mobile.login_page import MobileLoginPage
from pages.mobile.post_page import MobilePostPage
from utils import user

@pytest.fixture(scope="session")
def mobile_driver():
    """
    [Mobile] Appium iOS 18 시뮬레이터 픽스처
    - scope="session": 매 테스트마다 세션을 맺지 않고 한 번만 연결 (실행 속도 대폭 향상)
    """
    options = XCUITestOptions()
    options.platform_name = "iOS"
    options.device_name = "iPhone 18 Pro"
    options.udid = "189E5622-BA76-4EA5-8847-3BB6AC1A991F"
    options.automation_name = "XCUITest"
    
    # 플러터 빌드앱 절대경로
    options.app = "/Users/leeyr/Documents/GitHub/post/mobile/app/build/ios/iphonesimulator/Runner.app" 

    # 로컬 Appium 서버에 연결
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    # driver.implicitly_wait(10)  # BasePage 명시적 대기로 대체
    
    yield driver
    
    driver.quit()

@pytest.fixture(autouse=True)
def reset_app_state(mobile_driver):
    """
    세션은 유지하되, 각 테스트가 끝날 때마다 앱 프로세스만 빠르게 껐다 켭니다.
    """
    yield
    # 번들 ID를 이용해 앱을 강제 종료 후 재실행 (초고속 초기화)
    bundle_id = "com.example.app"
    mobile_driver.terminate_app(bundle_id)
    mobile_driver.activate_app(bundle_id)


@pytest.fixture
def mobile_logged_in(mobile_driver):
    """
    사전 조건: 테스트 실행 전 로그인 처리
    """
    login_page = MobileLoginPage(mobile_driver)
    login_page.enter_id(user.ID)
    login_page.enter_password(user.PWD)
    login_page.click_login()
    return mobile_driver

@pytest.fixture
def mobile_test_post_title(mobile_logged_in):
    """
    사전 조건: 로그인 후 임시 게시글 생성, 생성된 제목 반환
    """
    post_page = MobilePostPage(mobile_logged_in)
    post_page.click_write_fab()
    
    test_title = f"[Mobile] 임시글 {uuid.uuid4().hex[:5]}"
    post_page.enter_title(test_title)
    post_page.enter_content("사전 조건으로 자동 생성된 게시글입니다.")
    post_page.click_save_post()
    
    return test_title
