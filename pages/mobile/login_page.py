from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile.base_page import MobileBasePage

class MobileLoginPage(MobileBasePage):
    def enter_id(self, user_id):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "아이디"), user_id)
        
    def enter_password(self, password):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "비밀번호"), password)
        
    def click_login(self):
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "로그인"))
        
    def is_error_message_displayed(self, expected_text: str) -> bool:
        locator = (AppiumBy.XPATH, f"//*[contains(@label, '{expected_text}') or contains(@name, '{expected_text}') or contains(@value, '{expected_text}')]")
        return self.is_displayed(locator)

    def click_logout(self):
        self.click_element((AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, '로그아웃') or contains(@name, '로그아웃')]"))
        
    def is_login_screen_displayed(self) -> bool:
        return self.is_displayed((AppiumBy.ACCESSIBILITY_ID, "아이디"))
