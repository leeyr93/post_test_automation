from playwright.sync_api import Page
from utils import url

class FindPwPage:
    def __init__(self, page: Page):
        self.page = page

        self.title = page.locator("h3")
        self.id_input = page.locator("#id")
        self.name_input = page.locator("#name")
        self.email_input = page.locator("#email")
        self.submit_button = page.locator("form.login-form button.btn-primary")
        self.server_message = page.locator("section.messages p.text-danger")
        self.signup_link = page.locator("div.bottomlogin a[href='/join']")

    def open(self):
        self.page.goto(url.URL_FIND_PW)

    def fill_id(self, value: str):
        self.id_input.fill(value)

    def fill_name(self, value: str):
        self.name_input.fill(value)

    def fill_email(self, value: str):
        self.email_input.fill(value)

    def submit(self):
        self.submit_button.click()

    def find_pw(self, user_id: str = "", name: str = "", email: str = ""):
        self.fill_id(user_id)
        self.fill_name(name)
        self.fill_email(email)
        self.submit()

    def click_signup(self):
        self.signup_link.click()
