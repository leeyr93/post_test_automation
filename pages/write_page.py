class WritePage:
    def __init__(self, page):
        self.page = page
        self.title_input = page.locator("input[name='post_title']")
        self.content_input = page.locator("textarea[name='post_content']")
        self.submit_button = page.locator("button.btnwrite")

    def write_post(self, title, content):
        self.title_input.fill(title)
        self.content_input.fill(content)

    def submit_post(self):
        self.submit_button.click()