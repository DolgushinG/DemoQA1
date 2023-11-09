from pages.base_page import BasePage
from locators.forms_page_locators import FormsPageLocators


class FormsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self, url):
        self.browser.get(url)

    def click_practice_form(self):
        self.wait_and_click(FormsPageLocators.practice_form_btn)