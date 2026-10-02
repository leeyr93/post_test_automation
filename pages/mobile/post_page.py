from appium.webdriver.common.appiumby import AppiumBy

class MobilePostPage:
    def __init__(self, driver):
        self.driver = driver

    def click_write_fab(self):
        # 플러터의 FloatingActionButton
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "글쓰기").click()

    def enter_title(self, title):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "제목").send_keys(title)

    def enter_content(self, content):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내용을 입력하세요").send_keys(content)

    def click_save_post(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록하기").click()

    def open_post_by_title(self, title):
        # 방금 작성한 게시글의 제목을 찾아 클릭
        post_element = self.driver.find_element(AppiumBy.XPATH, f"(//*[contains(@label, '{title}') or contains(@name, '{title}')])[1]")
        post_element.click()

    def enter_comment(self, comment):
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeTextField").send_keys(comment + "\n")

    def click_submit_comment(self):
        try: self.driver.hide_keyboard()
        except: pass
        
        # 키보드 버튼을 찾을 때는 10초 대기를 무시하고 즉시(0초) 확인하도록 설정
        self.driver.implicitly_wait(0)
        try: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Done").click()
        except: pass
        try: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Return").click()
        except: pass
        self.driver.implicitly_wait(10) # 원래 대기 시간으로 복구
        
        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@label, '등록') or contains(@name, '등록')]").click()
