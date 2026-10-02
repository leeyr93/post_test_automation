from playwright.sync_api import Page
from utils import url

class FindIdPage:
    def __init__(self, page: Page):
        self.page = page

        self.title = page.locator("h3")
        self.name_input = page.locator("#name")
        self.email_input = page.locator("#email")
        self.submit_button = page.locator("form.login-form button.btn-primary")
        self.server_message = page.locator("section.messages p")
        self.signup_link = page.locator("div.bottomlogin a[href='/join']")

    def open(self):
        self.page.goto(url.URL_FIND_ID)

    def fill_name(self, value: str):
        self.name_input.fill(value)

    def fill_email(self, value: str):
        self.email_input.fill(value)

    def submit(self):
        self.submit_button.click()

    def find_id(self, name: str = "", email: str = ""):
        self.fill_name(name)
        self.fill_email(email)
        self.submit()

    def click_signup(self):
        self.signup_link.click()


class FindIdResultPage:
    def __init__(self, page: Page):
        self.page = page

        self.title = page.locator("h3")
        self.result_table = page.locator("table.table-bordered")
        self.result_id_rows = page.locator("table.table-bordered tr")
        self.result_ids = page.locator("table.table-bordered tr td:nth-child(2)")
        self.confirm_button = page.locator("button.btn-primary")
        self.login_button = page.locator("button#login a, a[href='/login']")
        self.signup_button = page.locator("button#join a, a[href='/join']")
        self.find_pw_button = page.locator("button#find_pw a, a[href='/find_pw']")

    def get_found_ids(self) -> list[str]:
        count = self.result_ids.count()
        return [self.result_ids.nth(i).inner_text().strip() for i in range(count)]

    def click_confirm(self):
        self.confirm_button.click()

    def click_login(self):
        self.login_button.click()

    def click_signup(self):
        self.signup_button.click()

    def click_find_pw(self):
        self.find_pw_button.click()
