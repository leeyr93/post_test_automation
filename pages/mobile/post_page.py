from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile.base_page import MobileBasePage

class MobilePostPage(MobileBasePage):
    def click_write_fab(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "글쓰기"))

    def enter_title(self, title):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "제목"), title)

    def enter_content(self, content):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "내용을 입력하세요"), content)

    def click_save_post(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "등록하기"))

    def open_post_by_title(self, title):
        self.click_element((AppiumBy.XPATH, f"(//*[contains(@label, '{title}') or contains(@name, '{title}')])[1]"))

    def enter_comment(self, comment):
        self.input_text((AppiumBy.XPATH, "//XCUIElementTypeTextField"), comment + "\n")

    def click_submit_comment(self):
        try: self.driver.hide_keyboard()
        except: pass
        
        # 키보드 버튼을 찾을 때는 명시적 대기(1초)만 수행 후 넘어가도록 처리
        try: self.click_element((AppiumBy.ACCESSIBILITY_ID, "Done"), timeout=1)
        except: pass
        try: self.click_element((AppiumBy.ACCESSIBILITY_ID, "Return"), timeout=1)
        except: pass
        
        self.click_element((AppiumBy.XPATH, "//*[contains(@label, '등록') or contains(@name, '등록')]"))

    def is_post_in_list(self, title: str) -> bool:
        return self.is_displayed((AppiumBy.XPATH, f"//*[contains(@label, '{title}') or contains(@name, '{title}')]"))

    def click_more_menu(self):
        btns = self.wait_for_elements((AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, 'Show menu') or contains(@name, 'Show menu')]"))
        if not btns:
            btns = self.wait_for_elements((AppiumBy.XPATH, "//XCUIElementTypeButton"))
        if btns:
            btns[-1].click()
            
    def is_more_menu_visible(self) -> bool:
        btns = self.wait_for_elements((AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, 'Show menu') or contains(@name, 'Show menu')]"), timeout=2)
        return len(btns) > 0

    def click_edit_post(self):
        self.click_element((AppiumBy.XPATH, "//*[contains(@label, '글 수정') or contains(@name, '글 수정')]"))
        
    def click_delete_post(self):
        self.click_element((AppiumBy.XPATH, "//*[contains(@label, '글 삭제') or contains(@name, '글 삭제')]"))

    def clear_title(self):
        elem = self.wait_for_element((AppiumBy.ACCESSIBILITY_ID, "제목"))
        elem.clear()
        
    def click_edit_complete(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "수정 완료"))

    def search_post(self, keyword: str):
        self.input_text((AppiumBy.XPATH, "//XCUIElementTypeTextField[contains(@value, '제목으로 검색하세요') or contains(@label, '제목으로 검색하세요')]"), keyword + "\n")
        
    def is_search_results_displayed(self) -> bool:
        btns = self.wait_for_elements((AppiumBy.XPATH, "//*[contains(@label, '조회수') or contains(@name, '조회수')]"), timeout=3)
        return len(btns) > 0

    def is_empty_search_message_displayed(self) -> bool:
        return self.is_displayed((AppiumBy.XPATH, "//*[contains(@label, '게시글이 없습니다.') or contains(@name, '게시글이 없습니다.')]"))

    def click_comment_more_menu(self):
        self.click_element((AppiumBy.XPATH, "//*[contains(@label, '댓글 더보기') or contains(@name, '댓글 더보기')]"))
        
    def click_edit_comment(self):
        self.click_element((AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, '수정') or contains(@name, '수정')]"))
        
    def click_delete_comment(self):
        self.click_element((AppiumBy.XPATH, "//*[contains(@label, '삭제') or contains(@name, '삭제')]"))

    def edit_comment(self, text: str):
        self.input_text((AppiumBy.XPATH, "//XCUIElementTypeTextField"), text)
        self.click_element((AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, '수정') or contains(@name, '수정') or contains(@label, '확인')]"))
        
    def is_comment_displayed(self, text: str) -> bool:
        return self.is_displayed((AppiumBy.XPATH, f"//*[contains(@label, '{text}') or contains(@name, '{text}')]"))
        
    def is_others_comment_more_visible(self, user_id: str) -> bool:
        btns = self.wait_for_elements((AppiumBy.XPATH, f"//*[contains(@label, '{user_id}')]/following::XCUIElementTypeButton[1]"), timeout=2)
        if not btns:
            return False
        # If button exists, click it and see if edit/delete is visible
        try:
            btns[0].click()
            menus = self.wait_for_elements((AppiumBy.XPATH, "//*[contains(@label, '수정') or contains(@label, '삭제')]"), timeout=2)
            return len(menus) > 0
        except Exception:
            return False

    def is_others_post_more_visible(self) -> bool:
        btns = self.wait_for_elements((AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, 'Show menu') or contains(@name, 'Show menu')]"), timeout=2)
        if not btns:
            btns = self.wait_for_elements((AppiumBy.XPATH, "//XCUIElementTypeButton"), timeout=2)
        if not btns:
            return False
            
        try:
            btns[-1].click()
            menus = self.wait_for_elements((AppiumBy.XPATH, "//*[contains(@label, '글 수정') or contains(@label, '글 삭제')]"), timeout=2)
            return len(menus) > 0
        except Exception:
            return False
