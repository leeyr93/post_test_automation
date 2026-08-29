from playwright.sync_api import expect
from pages.view_page import ViewPage
from services import post_service, comment_service
from utils import user


# 댓글 작성
def test_create_comment(page, precondition_post):
    precondition_post()
    target, post_comment = comment_service.comment_write(page)

    expect(target).to_contain_text(user.ID)
    expect(target).to_contain_text(post_comment)

    
# 댓글 수정
def test_edit_comment(page, precondition_post):
    precondition_post()
    comment_service.comment_write(page)
    comment = comment_service.search_comment(page)

    edit_btn = comment.locator("a:has-text('수정')")
    expect(edit_btn).to_be_visible()

    updated_comment = comment_service.comment_edit(page, comment)
    expect(updated_comment).to_be_visible()


# 댓글 삭제
def test_delete_comment(page, precondition_post):
    precondition_post()
    comment_service.comment_write(page)
    comment = comment_service.search_comment(page)

    delete_btn = comment.locator("a:has-text('삭제')")
    expect(delete_btn).to_be_visible()

    comment_text = comment_service.comment_delete(page, comment)
    expect(page.locator("tr").filter(has=page.get_by_text(comment_text, exact=True))).to_have_count(0)


# 내가 쓰지 않은 댓글 수정 여부 확인
def edit_other_comment(page):
    view = ViewPage(page)

    # 본인이 작성한 글, 본인이 작성하지 않은 댓글 > 댓글 수정 불가
    post_service.select_post(page, user.ID, True)
    comment = comment_service.search_comment(page, user.ID, False)
    edit_btn = comment.locator("a:has-text('수정')")
    expect(edit_btn).to_have_count(0)
    view.click_go_main() # 메인으로 이동하기

    # 본인이 작성하지 않은 글, 본인이 작성한 댓글 > 댓글 수정 가능
    post_service.select_post(page, user.ID, False) # 내가 작성하지 않은 게시글 선택
    comment = comment_service.search_comment(page)
    edit_btn = comment.locator("a:has-text('수정')")
    expect(edit_btn).to_be_visible()
    updated_comment = comment_service.comment_edit(page, comment)
    expect(updated_comment).to_be_visible()

    # 본인이 작성하지 않은 글, 본인이 작성하지 않은 댓글 > 댓글 수정 불가
    comment = comment_service.search_comment(page, user.ID, False)
    edit_btn = comment.locator("a:has-text('수정')")
    expect(edit_btn).to_have_count(0)


# 내가 쓰지 않은 댓글 삭제 여부 확인
def delete_other_comment(page):
    view = ViewPage(page)
    view.click_go_main() # 메인으로 이동하기

    # 본인이 작성한 글, 본인이 작성하지 않은 댓글 > 댓글 삭제 불가
    post_service.select_post(page, user.ID, True)
    comment = comment_service.search_comment(page, user.ID, False)
    delete_btn = comment.locator("a:has-text('삭제')")
    expect(delete_btn).to_have_count(0)
    view.click_go_main() # 메인으로 이동하기

    # 본인이 작성하지 않은 글, 본인이 작성한 댓글 > 댓글 삭제 가능
    post_service.select_post(page, user.ID, False) # 내가 작성하지 않은 게시글 선택
    comment = comment_service.search_comment(page)
    delete_btn = comment.locator("a:has-text('삭제')")
    expect(delete_btn).to_be_visible()

    comment_text = comment_service.comment_delete(page, comment)
    expect(page.locator("tr").filter(has=page.get_by_text(comment_text, exact=True))).to_have_count(0)

    # 본인이 작성하지 않은 글, 본인이 작성하지 않은 댓글 > 댓글 삭제 불가
    comment = comment_service.search_comment(page, user.ID, False)
    delete_btn = comment.locator("a:has-text('삭제')")
    expect(delete_btn).to_have_count(0)

# 내가 쓰지 않은 댓글 수정/삭제 여부 확인
def test_other_comment(page):
    comment_service.pre_condition_comment(page)

    edit_other_comment(page)
    delete_other_comment(page)