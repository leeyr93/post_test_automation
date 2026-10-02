from appium.webdriver.common.appiumby import AppiumBy

class MobileLoginPage:
    """
    모바일 플러터 앱용 로그인 페이지 객체(Page Object Model).
    웹(Playwright) 페이지 객체와 분리하여 AppiumBy를 사용합니다.
    """
    def __init__(self, driver):
        self.driver = driver
        
    def enter_id(self, user_id):
        # Flutter에서는 TextField의 labelText가 접근성 ID나 텍스트로 인식됩니다.
        # 실제 개발 시 Flutter의 Semantics(label: "아이디")를 추가하면 더욱 정확합니다.
        id_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아이디")
        id_field.send_keys(user_id)
        
    def enter_password(self, password):
        pw_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호")
        pw_field.send_keys(password)
        
    def click_login(self):
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass
        login_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_btn.click()
        
    def get_error_message(self):
        # 로그인 실패 시 나타나는 에러 텍스트 (예: "아이디와 비밀번호를 모두 입력해주세요.")
        error_elem = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@value, '입력해주세요')]")
        return error_elem.text
