import pytest, re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.find_id_page import FindIdPage, FindIdResultPage
from services import find_service, signup_service
from test_data.find_cases import FIND_ID_INVALID_CASES
from utils import url

# 1. 아이디 찾기 페이지 UI 기본 노출 및 placeholder 검증
def test_find_id_page_display(page):
    find_id_page = FindIdPage(page)
    find_id_page.open()

    expect(find_id_page.title).to_have_text("아이디 찾기")
    expect(find_id_page.name_input).to_be_visible()
    expect(find_id_page.name_input).to_have_attribute("placeholder", "이름을 입력해주세요.")

    expect(find_id_page.email_input).to_be_visible()
    expect(find_id_page.email_input).to_have_attribute("placeholder", "이메일을 입력해주세요.")

    expect(find_id_page.submit_button).to_be_visible()
    expect(find_id_page.signup_link).to_be_visible()


# 2. 로그인 페이지에서 아이디 찾기 링크 클릭 이동 검증
def test_navigate_to_find_id_from_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.click_find_id()
    expect(page).to_have_url(re.compile(r"/find_id$"))


# 3. 아이디 찾기 실패 케이스 검증 (존재하지 않는 회원, 빈 값, 불일치 등)
@pytest.mark.parametrize("case", FIND_ID_INVALID_CASES, ids=[c["name"] for c in FIND_ID_INVALID_CASES])
def test_find_id_invalid(page, case):
    find_id_page = FindIdPage(page)
    find_id_page.open()

    find_id_page.find_id(
        name=case["data"]["name"],
        email=case["data"]["email"]
    )
    expect(find_id_page.server_message).to_be_visible()
    expect(find_id_page.server_message).to_have_text(case["expected"]["message"])


# 4. 아이디 찾기 성공 케이스 검증
def test_find_id_success(page):
    user = signup_service.register_user(page)

    result_page = find_service.find_id(
        page,
        name=user["name"],
        email=user["email"]
    )

    expect(result_page.title).to_have_text("아이디 찾기 결과")
    expect(result_page.result_table).to_be_visible()
    expect(result_page.result_table).to_contain_text(user["user_id"])


# 5. 아이디 찾기 결과 페이지의 확인 버튼(메인 이동) 동작 검증
def test_find_id_result_confirm_button(page):
    user = signup_service.register_user(page)

    result_page = find_service.find_id(
        page,
        name=user["name"],
        email=user["email"]
    )
    result_page.click_confirm()
    expect(page).to_have_url(re.compile(r"/board_list(?:\?.*)?$"))


# 6. 아이디 찾기 결과 페이지의 하단 이동 링크(로그인, 회원가입, 비밀번호 찾기) 동작 검증
def test_find_id_result_links(page):
    user = signup_service.register_user(page)

    # 로그인 링크 이동
    result_page = find_service.find_id(
        page,
        name=user["name"],
        email=user["email"]
    )
    result_page.click_login()
    expect(page).to_have_url(re.compile(r"/login$"))

    # 회원가입 링크 이동
    result_page = find_service.find_id(
        page,
        name=user["name"],
        email=user["email"]
    )
    result_page.click_signup()
    expect(page).to_have_url(re.compile(r"/join$"))

    # 비밀번호 찾기 링크 이동
    result_page = find_service.find_id(
        page,
        name=user["name"],
        email=user["email"]
    )
    result_page.click_find_pw()
    expect(page).to_have_url(re.compile(r"/find_pw$"))

