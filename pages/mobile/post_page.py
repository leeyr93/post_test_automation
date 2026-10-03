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
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "comment_input"), comment + "\n")

    def click_submit_comment(self):
        try: self.driver.hide_keyboard()
        except: pass
        
        # 키보드 버튼을 찾을 때는 명시적 대기(1초)만 수행 후 넘어가도록 처리
        try: self.click_element((AppiumBy.ACCESSIBILITY_ID, "Done"), timeout=1)
        except: pass
        try: self.click_element((AppiumBy.ACCESSIBILITY_ID, "Return"), timeout=1)
        except: pass
        
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "comment_submit_btn"))

    def is_post_in_list(self, title: str) -> bool:
        return self.is_displayed((AppiumBy.XPATH, f"//*[contains(@label, '{title}') or contains(@name, '{title}')]"))

    def click_more_menu(self):
        # [리팩터링] 기본 tooltip(Show menu) 의존 제거. 앱에서 부여한 ID 사용
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "post_more_btn"))
            
    def is_more_menu_visible(self) -> bool:
        return self.is_displayed((AppiumBy.ACCESSIBILITY_ID, "post_more_btn"), timeout=2)

    def click_edit_post(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "post_menu_edit"))
        
    def click_delete_post(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "post_menu_delete"))

    def clear_title(self):
        elem = self.wait_for_element((AppiumBy.ACCESSIBILITY_ID, "제목"))
        elem.clear()
        
    def click_edit_complete(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "수정 완료"))

    def search_post(self, keyword: str):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "search_input"), keyword + "\n")
        
    def is_search_results_displayed(self) -> bool:
        # [리팩터링] Appium은 ACCESSIBILITY_ID 정규식을 지원하지 않으므로, 
        # 대신 iOS/Android 공통적으로 label이 "post_item_"으로 시작하는 요소를 XPATH로 찾거나 
        # 그냥 ListView 자체에 ID를 주는 것이 좋음. 여기선 ListView 자체를 찾도록 수정 가능하지만
        # 임시로 starts-with 사용
        btns = self.wait_for_elements((AppiumBy.ACCESSIBILITY_ID, "search_results_list"), timeout=3)
        return len(btns) > 0

    def is_empty_search_message_displayed(self) -> bool:
        return self.is_displayed((AppiumBy.ACCESSIBILITY_ID, "empty_result_msg"))

    def click_edit_comment(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "comment_menu_edit"))
        
    def click_delete_comment(self):
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "comment_menu_delete"))

    def edit_comment(self, text: str):
        self.input_text((AppiumBy.ACCESSIBILITY_ID, "edit_comment_input"), text)
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "edit_comment_submit_btn"))
        
    def is_comment_displayed(self, text: str) -> bool:
        return self.is_displayed((AppiumBy.ACCESSIBILITY_ID, f"comment_content_{text}"))
        
    def is_others_comment_more_visible(self, comment_text: str) -> bool:
        # [리팩터링] 고유 ID를 부여했으므로 버튼 존재 자체가 버그임. 바로 노출 여부 반환.
        return self.is_displayed((AppiumBy.ACCESSIBILITY_ID, f"comment_more_btn_{comment_text}"), timeout=2)

    def is_others_post_more_visible(self) -> bool:
        # [리팩터링] 고유 ID를 부여했으므로 버튼 존재 자체가 버그임. 바로 노출 여부 반환.
        return self.is_displayed((AppiumBy.ACCESSIBILITY_ID, "post_more_btn"), timeout=2)
