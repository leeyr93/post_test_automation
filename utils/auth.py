from playwright.sync_api import expect
from pages.login_page import LoginPage
from utils import url

def login(page, user_id, password):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(user_id, password)
    expect(page).to_have_url(url.URL_BOARD_LIST)