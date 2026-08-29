from playwright.sync_api import Page
from utils import url

class PostPage:
    def __init__(self, page: Page):
        self.page = page

        # 버튼
        self.login_button = page.locator("a[href='/login']")
        self.logout_button = page.locator("a[href='/logout']")
        self.write_button = page.locator("a[href='/board_write']")

        # 검색
        self.search_input = page.locator("input[name='boardSearch']")
        self.search_button = page.locator("form[action='/board_search'] button[type='submit']")

        # 게시글
        self.post_rows = page.locator("table tbody tr")

        # 빈 결과
        self.empty_message = page.locator("h3", has_text="검색결과가 존재하지 않습니다.")
        self.move_to_list_link = page.locator("a", has_text="게시글 목록으로 이동")

        # 게시글 삭제 모달
        self.delete_modal = page.locator("#boardModal")
        self.delete_confirm_button = self.delete_modal.locator("a.btn-primary:has-text('확인')")
        self.delete_message = self.delete_modal.locator("text=해당 글을 삭제하시겠습니까?")


    # ===== 액션 =====
    def open(self):
        self.page.goto(url.URL_BOARD_LIST)

    def click_login(self):
        self.login_button.click()

    def click_logout(self):
        self.logout_button.click()

    def click_write(self):
        self.write_button.click()

    def search(self, keyword: str):
        self.search_input.fill(keyword)
        self.search_button.click()

    def click_move_to_list(self):
        self.move_to_list_link.click()

    def delete_modal_wait_visible(self):
        self.delete_modal.wait_for(state="visible")

    def delete_confirm(self):
        self.delete_confirm_button.click()

    def get_column_index(self, column_name: str):
        headers = self.page.locator("table thead th")

        for i in range(headers.count()):
            if headers.nth(i).inner_text().strip() == column_name:
                return i + 1

        raise Exception(f"{column_name} 컬럼을 찾을 수 없습니다.")

    def find_post_row(self, column_name: str, value: str):
        col_index = self.get_column_index(column_name)

        return self.post_rows.filter(
            has=self.page.locator(f"td:nth-child({col_index})", has_text=value)
        )

    def click_post(self, title: str):
        self.find_post_row("제목", title).first.click()

    def find_post_by_title(self, title: str):
        return self.post_rows.filter(
            has=self.page.locator("td", has_text=title)
        )

    def find_post_by_writer(self, writer: str):
        writer_col = self.get_column_index("작성자")

        rows = self.post_rows
        for i in range(rows.count()):
            row = rows.nth(i)
            writer_text = row.locator(f"td:nth-child({writer_col})").inner_text().strip()

            if writer_text == writer:
                return row

        return None