import allure
from playwright.sync_api import expect
from pages.view_page import ViewPage
from services import post_service, comment_service
from utils import user

@allure.id("TC-66")
@allure.title("상세 페이지에서 댓글 작성 시 노출 확인")
def test_create_comment(page, precondition_post):
    precondition_post()
    target, post_comment = comment_service.comment_write(page)

    expect(target).to_contain_text(user.ID)
    expect(target).to_contain_text(post_comment)


@allure.id("TC-67")
@allure.title("본인 작성 댓글 내용 수정 및 반영 확인")
def test_edit_comment(page, precondition_post):
    precondition_post()
    comment_service.comment_write(page)
    comment = comment_service.search_comment(page)

    edit_btn = comment.locator("a:has-text('수정')")
    expect(edit_btn).to_be_visible()

    updated_comment = comment_service.comment_edit(page, comment)
    expect(updated_comment).to_be_visible()


@allure.id("TC-68")
@allure.title("본인 작성 댓글 삭제 및 목록 제거 확인")
def test_delete_comment(page, precondition_post):
    precondition_post()
    comment_service.comment_write(page)
    comment = comment_service.search_comment(page)

    delete_btn = comment.locator("a:has-text('삭제')")
    expect(delete_btn).to_be_visible()

    comment_text = comment_service.comment_delete(page, comment)
    expect(page.locator("tr").filter(has=page.get_by_text(comment_text, exact=True))).to_have_count(0)


@allure.id("TC-69")
@allure.title("내 글 - 타인 댓글 [수정] 버튼 미노출 확인")
def test_cannot_edit_others_comment_on_my_post(page):
    comment_service.pre_condition_comment(page)
    
    # 본인이 작성한 글, 본인이 작성하지 않은 댓글 > 댓글 수정 불가
    post_service.select_post(page, user.ID, True)
    comment = comment_service.search_comment(page, user.ID, False)
    edit_btn = comment.locator("a:has-text('수정')")
    expect(edit_btn).to_have_count(0)


@allure.id("TC-70")
@allure.title("내 글 - 타인 댓글 [삭제] 버튼 미노출 확인")
def test_cannot_delete_others_comment_on_my_post(page):
    comment_service.pre_condition_comment(page)
    
    # 본인이 작성한 글, 본인이 작성하지 않은 댓글 > 댓글 삭제 불가
    post_service.select_post(page, user.ID, True)
    comment = comment_service.search_comment(page, user.ID, False)
    delete_btn = comment.locator("a:has-text('삭제')")
    expect(delete_btn).to_have_count(0)


@allure.id("TC-71")
@allure.title("타인 글 - 내 댓글 [수정] 가능 확인")
def test_can_edit_my_comment_on_others_post(page):
    comment_service.pre_condition_comment(page)
    
    # 본인이 작성하지 않은 글, 본인이 작성한 댓글 > 댓글 수정 가능
    post_service.select_post(page, user.ID, False)
    comment = comment_service.search_comment(page)
    edit_btn = comment.locator("a:has-text('수정')")
    expect(edit_btn).to_be_visible()
    
    updated_comment = comment_service.comment_edit(page, comment)
    expect(updated_comment).to_be_visible()


@allure.id("TC-72")
@allure.title("타인 글 - 내 댓글 [삭제] 가능 확인")
def test_can_delete_my_comment_on_others_post(page):
    comment_service.pre_condition_comment(page)
    
    # 본인이 작성하지 않은 글, 본인이 작성한 댓글 > 댓글 삭제 가능
    post_service.select_post(page, user.ID, False)
    comment = comment_service.search_comment(page)
    delete_btn = comment.locator("a:has-text('삭제')")
    expect(delete_btn).to_be_visible()

    comment_text = comment_service.comment_delete(page, comment)
    expect(page.locator("tr").filter(has=page.get_by_text(comment_text, exact=True))).to_have_count(0)


@allure.id("TC-73")
@allure.title("타인 글 - 타인 댓글 [수정] 버튼 미노출 확인")
def test_cannot_edit_others_comment_on_others_post(page):
    comment_service.pre_condition_comment(page)
    
    # 타인의 글 진입 후 타인의 댓글 겟
    post_service.select_post(page, user.ID, False)
    comment = comment_service.search_comment(page, user.ID, False)
    edit_btn = comment.locator("a:has-text('수정')")
    expect(edit_btn).to_have_count(0)


@allure.id("TC-74")
@allure.title("타인 글 - 타인 댓글 [삭제] 버튼 미노출 확인")
def test_cannot_delete_others_comment_on_others_post(page):
    comment_service.pre_condition_comment(page)
    
    # 타인의 글 진입 후 타인의 댓글 겟
    post_service.select_post(page, user.ID, False)
    comment = comment_service.search_comment(page, user.ID, False)
    delete_btn = comment.locator("a:has-text('삭제')")
    expect(delete_btn).to_have_count(0)
