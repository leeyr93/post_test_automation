from playwright.sync_api import Page
from utils import url

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.id_input= page.locator("input[name='id']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("button#login")
        self.error_message = page.locator("section.messages p.text-danger")

    def open(self):
        self.page.goto(url.URL_LOGIN)

    def login(self, user_id, password):
        self.id_input.fill(user_id)
        self.password_input.fill(password)
        self.login_button.click()
