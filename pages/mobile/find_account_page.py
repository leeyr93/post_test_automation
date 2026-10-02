from appium.webdriver.common.appiumby import AppiumBy

class MobileFindAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def click_find_account_link(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "계정 찾기 (ID/PW)").click()

    def switch_to_find_id(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아이디 찾기").click()

    def switch_to_reset_pw(self):
        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@label, '비밀번호 재설정') or contains(@name, '비밀번호 재설정')]").click()

    def enter_id(self, user_id):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "가입한 아이디").send_keys(user_id)

    def enter_name(self, name):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "가입한 이름").send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "가입한 이메일").send_keys(email)

    def click_find_id_button(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아이디 찾기").click()

    def click_verify_user_button(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원 정보 확인").click()

    def get_error_message(self):
        # 입력 안내 또는 오류 메시지 요소 찾기
        error_elem = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@label, '입력') or contains(@name, '입력') or contains(@value, '입력')]")
        return error_elem.text
