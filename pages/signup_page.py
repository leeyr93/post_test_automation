from playwright.sync_api import Page
from utils import url

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
    
        self.user_id = page.locator("#userId")
        self.password = page.locator("#password")
        self.repassword = page.locator("#repassword")
        self.user_name = page.locator("#userName")
        self.email = page.locator("#email")
        self.submit_button = page.locator("form.login-form button")
        self.server_message = page.locator("section.messages p")

    def open(self):
        self.page.goto(url.URL_SIGNUP)

    def fill_id(self, value: str):
        self.user_id.fill(value)

    def fill_password(self, value: str):
        self.password.fill(value)

    def fill_repassword(self, value: str):
        self.repassword.fill(value)

    def fill_name(self, value: str):
        self.user_name.fill(value)

    def fill_email(self, value: str):
        self.email.fill(value)

    def submit(self):
        self.submit_button.click()
    
    def signup(self, user_id="", password="", repassword="", name="", email=""):
        self.fill_id(user_id)
        self.fill_password(password)
        self.fill_repassword(repassword)
        self.fill_name(name)
        self.fill_email(email)
        self.submit()
