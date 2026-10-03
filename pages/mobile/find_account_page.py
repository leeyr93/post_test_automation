from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile.base_page import MobileBasePage

class MobileFindAccountPage(MobileBasePage):
    def click_find_account_link(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "계정 찾기 (ID/PW)"))

    def switch_to_find_id(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "아이디 찾기"))

    def switch_to_reset_pw(self):
        self.click_element((AppiumBy.XPATH, "//*[contains(@label, '비밀번호 재설정') or contains(@name, '비밀번호 재설정')]"))

    def enter_id(self, user_id):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "가입한 아이디"), user_id)

    def enter_name(self, name):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "가입한 이름"), name)

    def enter_email(self, email):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "가입한 이메일"), email)

    def click_find_id_button(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "아이디 찾기"))

    def click_verify_user_button(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "회원 정보 확인"))

    def is_error_message_displayed(self, expected_text: str) -> bool:
        # XPath 문법 오류(single quote 중첩)를 피하기 위해 expected_text에 '가 있으면 쌍따옴표로 감쌉니다.
        if "'" in expected_text:
            xpath = f'//*[contains(@label, "{expected_text}") or contains(@name, "{expected_text}") or contains(@value, "{expected_text}")]'
        else:
            xpath = f"//*[contains(@label, '{expected_text}') or contains(@name, '{expected_text}') or contains(@value, '{expected_text}')]"
        return self.is_displayed((AppiumBy.XPATH, xpath))

    def is_result_displayed(self, expected_id: str) -> bool:
        return self.is_displayed((AppiumBy.XPATH, f"//*[contains(@label, '{expected_id}') or contains(@name, '{expected_id}')]"))
