from playwright.sync_api import Page
from pages.find_id_page import FindIdPage, FindIdResultPage
from pages.find_pw_page import FindPwPage
from pages.reset_pw_page import ResetPwPage

def find_id(page: Page, name: str, email: str) -> FindIdResultPage:
    find_id_page = FindIdPage(page)
    find_id_page.open()
    find_id_page.find_id(name=name, email=email)
    return FindIdResultPage(page)

def find_pw(page: Page, user_id: str, name: str, email: str) -> ResetPwPage:
    find_pw_page = FindPwPage(page)
    find_pw_page.open()
    find_pw_page.find_pw(user_id=user_id, name=name, email=email)
    return ResetPwPage(page)

def reset_pw(page: Page, password: str, repassword: str):
    reset_pw_page = ResetPwPage(page)
    reset_pw_page.reset_password(password=password, repassword=repassword)

def find_pw_and_reset(page: Page, user_id: str, name: str, email: str, new_password: str, repassword: str):
    find_pw(page, user_id, name, email)
    reset_pw(page, new_password, repassword)
