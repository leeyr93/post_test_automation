import pytest, re, allure
from playwright.sync_api import expect
from pages.find_id_page import FindIdPage, FindIdResultPage
from services import find_service, signup_service
from test_data.find_cases import FIND_ID_INVALID_CASES

@allure.id("TC-36")
@allure.title("아이디 찾기 페이지 UI 확인")
def test_find_id_page_display(page):
    find_id_page = FindIdPage(page)
    find_id_page.open()

    expect(find_id_page.name_input).to_be_visible()
    expect(find_id_page.name_input).to_have_attribute("placeholder", "이름을 입력해주세요.")

    expect(find_id_page.email_input).to_be_visible()
    expect(find_id_page.email_input).to_have_attribute("placeholder", "이메일을 입력해주세요.")

    expect(find_id_page.submit_button).to_be_visible()
    expect(find_id_page.signup_link).to_be_visible()

@pytest.mark.parametrize("case", FIND_ID_INVALID_CASES, ids=[c["name"] for c in FIND_ID_INVALID_CASES])
def test_find_id_invalid(page, case):
    allure.dynamic.id(case.get("tc_id"))
    allure.dynamic.title(case.get("tc_title"))

    find_id_page = FindIdPage(page)
    find_id_page.open()

    find_id_page.find_id(
        name=case["data"]["name"],
        email=case["data"]["email"]
    )
    expect(find_id_page.server_message).to_be_visible()
    expect(find_id_page.server_message).to_have_text(case["expected"]["message"])

@allure.id("TC-42")
@allure.title("일치 정보 입력 시 아이디 찾기 성공 및 노출 확인")
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

@allure.id("TC-43")
@allure.title("결과 페이지 [확인] 버튼 클릭 시 메인 이동 확인")
def test_find_id_result_confirm_button(page):
    user = signup_service.register_user(page)

    result_page = find_service.find_id(
        page,
        name=user["name"],
        email=user["email"]
    )
    result_page.click_confirm()
    expect(page).to_have_url(re.compile(r"/board_list(?:\?.*)?$"))

@allure.id("TC-44")
@allure.title("로그인 이동 텍스트 확인")
def test_find_id_result_login_link(page):
    user = signup_service.register_user(page)
    result_page = find_service.find_id(
        page,
        name=user["name"],
        email=user["email"]
    )
    result_page.click_login()
    expect(page).to_have_url(re.compile(r"/login$"))

@allure.id("TC-45")
@allure.title("회원가입 텍스트 링크 확인")
def test_find_id_result_signup_link(page):
    user = signup_service.register_user(page)
    result_page = find_service.find_id(
        page,
        name=user["name"],
        email=user["email"]
    )
    result_page.click_signup()
    expect(page).to_have_url(re.compile(r"/join$"))

@allure.id("TC-46")
@allure.title("비밀번호 찾기 텍스트 링크 확인")
def test_find_id_result_find_pw_link(page):
    user = signup_service.register_user(page)
    result_page = find_service.find_id(
        page,
        name=user["name"],
        email=user["email"]
    )
    result_page.click_find_pw()
    expect(page).to_have_url(re.compile(r"/find_pw$"))
