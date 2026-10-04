from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

class MobileBasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def _resolve_locator(self, locator: tuple) -> tuple:
        """
        안드로이드(UiAutomator2)와 iOS(XCUITest) 간의 Flutter 요소 렌더링 차이를
        해소하기 위해 locator를 동적으로 변환합니다.
        """
        by, value = locator
        platform = self.driver.capabilities.get("platformName", "").lower()
        
        if platform == "android" and by == AppiumBy.ACCESSIBILITY_ID:
            if "'" in value:
                xpath = f'//*[@hint="{value}" or @content-desc="{value}" or @text="{value}" or @resource-id="{value}"]'
            else:
                xpath = f"//*[@hint='{value}' or @content-desc='{value}' or @text='{value}' or @resource-id='{value}']"
            return (AppiumBy.XPATH, xpath)
        elif platform == "ios" and by == AppiumBy.ACCESSIBILITY_ID:
            # iOS에서는 focus 시 label에 hint 텍스트가 병합되어 exact match가 실패할 수 있으므로,
            # 시작 부분 일치(BEGINSWITH)로 탐색하도록 변경합니다.
            if "'" in value:
                predicate = f'name BEGINSWITH "{value}" OR label BEGINSWITH "{value}"'
            else:
                predicate = f"name BEGINSWITH '{value}' OR label BEGINSWITH '{value}'"
            return (AppiumBy.IOS_PREDICATE, predicate)
            
        return locator

    def wait_for_element(self, locator: tuple, timeout: int = None):
        """요소가 DOM에 나타날 때까지 명시적으로 대기합니다."""
        locator = self._resolve_locator(locator)
        t = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.driver, t).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_elements(self, locator: tuple, timeout: int = None):
        """여러 요소가 DOM에 나타날 때까지 대기합니다."""
        locator = self._resolve_locator(locator)
        t = timeout if timeout is not None else self.timeout
        try:
            return WebDriverWait(self.driver, t).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            return []

    def wait_for_invisible(self, locator: tuple, timeout: int = None):
        """요소가 사라질 때까지 대기합니다."""
        locator = self._resolve_locator(locator)
        t = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.driver, t).until(
            EC.invisibility_of_element_located(locator)
        )

    def click_element(self, locator: tuple, timeout: int = None):
        """요소를 기다린 후 클릭합니다."""
        locator = self._resolve_locator(locator)
        try:
            element = self.wait_for_element(locator, timeout)
            element.click()
        except StaleElementReferenceException:
            # Stale element 발생 시 한 번 더 시도
            element = self.wait_for_element(locator, timeout)
            element.click()

    def input_text(self, locator: tuple, text: str, timeout: int = None):
        """요소를 기다린 후 텍스트를 입력합니다."""
        locator = self._resolve_locator(locator)
        platform = self.driver.capabilities.get("platformName", "").lower()
        try:
            element = self.wait_for_element(locator, timeout)
            if platform == "android":
                element.click()
            element.clear()
            element.send_keys(text)
        except StaleElementReferenceException:
            element = self.wait_for_element(locator, timeout)
            if platform == "android":
                element.click()
            element.clear()
            element.send_keys(text)

    def get_text(self, locator: tuple, timeout: int = None) -> str:
        """요소를 기다린 후 텍스트 속성을 반환합니다."""
        locator = self._resolve_locator(locator)
        element = self.wait_for_element(locator, timeout)
        return element.text

    def is_displayed(self, locator: tuple, timeout: int = None) -> bool:
        """요소가 화면에 보이는지 여부를 반환합니다 (Timeout 발생 시 False)."""
        locator = self._resolve_locator(locator)
        try:
            self.wait_for_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    def input_text_active(self, locator: tuple, text: str, timeout: int = None):
        """요소에 클릭으로 포커스를 준 뒤, 활성 요소(active_element)를 통해 입력합니다."""
        locator = self._resolve_locator(locator)
        element = self.wait_for_element(locator, timeout)
        try:
            element.click()
        except Exception:
            pass
        self.driver.switch_to.active_element.send_keys(text)
