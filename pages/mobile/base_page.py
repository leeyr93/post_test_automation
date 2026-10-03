from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class MobileBasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element(self, locator: tuple, timeout: int = None):
        """요소가 DOM에 나타날 때까지 명시적으로 대기합니다."""
        t = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.driver, t).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_elements(self, locator: tuple, timeout: int = None):
        """여러 요소가 DOM에 나타날 때까지 대기합니다."""
        t = timeout if timeout is not None else self.timeout
        try:
            return WebDriverWait(self.driver, t).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            return []

    def wait_for_invisible(self, locator: tuple, timeout: int = None):
        """요소가 사라질 때까지 대기합니다."""
        t = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.driver, t).until(
            EC.invisibility_of_element_located(locator)
        )

    def click_element(self, locator: tuple, timeout: int = None):
        """요소를 기다린 후 클릭합니다."""
        element = self.wait_for_element(locator, timeout)
        element.click()

    def input_text(self, locator: tuple, text: str, timeout: int = None):
        """요소를 기다린 후 텍스트를 입력합니다."""
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple, timeout: int = None) -> str:
        """요소를 기다린 후 텍스트 속성을 반환합니다."""
        element = self.wait_for_element(locator, timeout)
        return element.text

    def is_displayed(self, locator: tuple, timeout: int = None) -> bool:
        """요소가 화면에 보이는지 여부를 반환합니다 (Timeout 발생 시 False)."""
        try:
            self.wait_for_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    def input_text_active(self, locator: tuple, text: str, timeout: int = None):
        """요소에 클릭으로 포커스를 준 뒤, 활성 요소(active_element)를 통해 입력합니다.
        (Flutter 문자 수 카운터 등으로 인한 StaleElementReferenceException 방지용)"""
        element = self.wait_for_element(locator, timeout)
        try:
            element.click()
        except Exception:
            pass
        self.driver.switch_to.active_element.send_keys(text)
