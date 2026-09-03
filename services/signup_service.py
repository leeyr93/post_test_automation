from playwright.sync_api import Page
from pages.signup_page import SignupPage
from test_data.signup_cases import get_valid_user_data
from utils import url

def perform_signup(signup_page, data: dict):
    signup_page.signup(
        user_id=data["user_id"],
        password=data["password"],
        repassword=data["repassword"],
        name=data["name"],
        email=data["email"]
    )

def register_user(page: Page, **overrides) -> dict:
    """
    고유한 랜덤 계정(또는 지정된 정보)으로 회원가입을 수행하고 유저 정보를 반환하는 헬퍼 함수
    """
    user_data = get_valid_user_data(**overrides)
    signup_page = SignupPage(page)
    signup_page.open()
    perform_signup(signup_page, user_data)
    page.wait_for_url(url.URL_LOGIN)
    return user_data