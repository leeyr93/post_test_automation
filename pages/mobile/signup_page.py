from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from appium.webdriver.common.appiumby import AppiumBy

class MobileSignupPage:
    def __init__(self, driver):
        self.driver = driver
        
    def click_signup_link(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").click()

    def enter_id(self, user_id):
        # 화면 전환 애니메이션을 기다리고, 요소를 탭하여 포커스를 맞춘 뒤 active_element에 직접 입력
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "아이디"))
        )
        try:
            elem.click()
        except Exception:
            pass # Stale 시도 무시, 이미 포커스 됐을 수 있음
        
        # 키보드 입력은 활성화된 요소에 직접 전달하여 StaleElementReferenceException 원천 차단
        self.driver.switch_to.active_element.send_keys(user_id)

    def scroll_down(self):
        try:
            # 키보드 버튼을 찾을 때는 10초 대기를 무시하고 즉시(0초) 확인하도록 설정
            self.driver.implicitly_wait(0)
            try: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Done").click()
            except: pass
            try: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Return").click()
            except: pass
            self.driver.implicitly_wait(10) # 원래 대기 시간으로 복구
            
            # iOS XCUITest의 가장 안정적인 네이티브 스크롤
            self.driver.execute_script("mobile: scroll", {"direction": "down"})
        except Exception:
            pass

    def enter_name(self, name):
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "이름"))
        )
        try:
            elem.click()
        except Exception:
            pass
        self.driver.switch_to.active_element.send_keys(name)

    def enter_email(self, email):
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "이메일"))
        )
        try:
            elem.click()
        except Exception:
            pass
        self.driver.switch_to.active_element.send_keys(email)

    def enter_password(self, pw):
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "비밀번호"))
        )
        try:
            elem.click()
        except Exception:
            pass
        self.driver.switch_to.active_element.send_keys(pw)

    def enter_password_confirm(self, pw):
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "비밀번호 확인"))
        )
        try:
            elem.click()
        except Exception:
            pass
        self.driver.switch_to.active_element.send_keys(pw)

    def click_submit(self):
        self.scroll_down()
        # 앱바 타이틀이 아닌 하단의 실제 전송 버튼을 클릭
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@name='회원가입' or @label='회원가입']").click()

    def get_error_message(self):
        error_elem = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@label, '입력') or contains(@name, '입력') or contains(@value, '입력') or contains(@label, '일치') or contains(@name, '일치')]")
        return error_elem.text
