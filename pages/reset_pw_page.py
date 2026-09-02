from playwright.sync_api import Page
from utils import url

class ResetPwPage:
    def __init__(self, page: Page):
        self.page = page

        self.title = page.locator("h3")
        self.id_hidden_input = page.locator("input[name='id'][type='hidden']")
        self.password_input = page.locator("#password")
        self.repassword_input = page.locator("#repassword")
        self.submit_button = page.locator("form.login-form button.btn-primary")
        self.server_message = page.locator("section.messages p.text-danger")

    def open(self, user_id: str = ""):
        target_url = f"{url.URL_RESET_PW}?id={user_id}" if user_id else url.URL_RESET_PW
        self.page.goto(target_url)

    def fill_password(self, value: str):
        self.password_input.fill(value)

    def fill_repassword(self, value: str):
        self.repassword_input.fill(value)

    def submit(self):
        self.submit_button.click()

    def reset_password(self, password: str = "", repassword: str = ""):
        self.fill_password(password)
        self.fill_repassword(repassword)
        self.submit()
