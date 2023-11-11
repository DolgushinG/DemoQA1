import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.browser.get(url)

    @allure.step("Скроллим страницу")
    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, 200)")

    @allure.step("Кликаем по разделу формы")
    def click_main_btn_forms(self):
        self.wait_and_click(MainPageLocators.main_btn_forms)

