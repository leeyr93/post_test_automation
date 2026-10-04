from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile.base_page import MobileBasePage

class MobileSignupPage(MobileBasePage):
        
    def click_signup_link(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "회원가입"))

    def enter_id(self, user_id):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "아이디"), user_id)

    def scroll_down(self):
        try:
            # 명시적 대기로 키보드 내리기 시도
            try: self.click_element((AppiumBy.ACCESSIBILITY_ID, "Done"), timeout=1)
            except: pass
            try: self.click_element((AppiumBy.ACCESSIBILITY_ID, "Return"), timeout=1)
            except: pass
            
            self.driver.execute_script("mobile: scroll", {"direction": "down"})
        except Exception:
            pass

    def enter_name(self, name):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "이름"), name)

    def enter_email(self, email):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "이메일"), email)

    def enter_password(self, pw):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "비밀번호"), pw)

    def enter_password_confirm(self, pw):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "비밀번호 확인"), pw)

    def click_submit(self):
        self.scroll_down()
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "btn_submit_signup"))

    def is_error_message_displayed(self, expected_text: str) -> bool:
        # XPath 문법 오류(single quote 중첩)를 피하기 위해 expected_text에 '가 있으면 쌍따옴표로 감쌉니다.
        if "'" in expected_text:
            xpath = f'//*[contains(@label, "{expected_text}") or contains(@name, "{expected_text}") or contains(@value, "{expected_text}") or contains(@text, "{expected_text}") or contains(@content-desc, "{expected_text}")]'
        else:
            xpath = f"//*[contains(@label, '{expected_text}') or contains(@name, '{expected_text}') or contains(@value, '{expected_text}') or contains(@text, '{expected_text}') or contains(@content-desc, '{expected_text}')]"
        return self.is_displayed((AppiumBy.XPATH, xpath))
