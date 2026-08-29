class ViewPage:
    def __init__(self, page):
        self.page = page
        self.edit_button = self.page.locator("a:has-text('글수정')") # 글 수정 버튼
        self.go_main_button = self.page.locator("a:has-text('메인으로 돌아가기')") # 메인으로 돌아가기 버튼
        self.delete_button = self.page.locator("a:has-text('글삭제')") # 글 삭제 버튼
        self.comment_input = page.locator("textarea[name='comm_content']") #댓글 입력 필드
        self.comment_button = page.locator("input[type='submit'][value='등록']") #댓글 등록 버튼

    # 글 수정 버튼 클릭
    def click_edit(self): 
        self.edit_button.click() 

    # 메인으로 돌아가기 버튼 클릭
    def click_go_main(self): 
        self.go_main_button.click()

    # 삭제 버튼 클릭
    def click_delete(self):
        self.delete_button.click()

    # 댓글 입력
    def write_comment(self, comment):
        self.comment_input.fill(comment)

    # 댓글 등록 버튼 클릭
    def click_comment(self):
        self.comment_button.click()
