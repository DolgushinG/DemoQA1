#from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import datetime



class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
    def open(self, url):
        self.browser.get(url)
    def _element_is_located(self, locator: tuple) -> WebElement:
        return Wait(self.browser, 20).until(EC.visibility_of_element_located(locator))

    def _element_is_clickabe(self, locator: tuple) -> WebElement:
        return Wait(self.browser, 20).until(EC.element_to_be_clickable(locator))




    def wait_and_fill_in(self, locator: tuple, text: str):
        self._element_is_located(locator).send_keys(text)

    def wait_and_click(self, locator: tuple):
        self._element_is_clickabe(locator)
        self.browser.find_element(*locator).click()

    def get_text(self, locator: tuple):
        return self.browser.find_element(*locator).text


    def take_screenshot(self):
        actual_time = datetime. datetime.utcnow().strftime ("%Y .%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + actual_time + ".png"
        self.browser.save_screenshot('/Users/sasha17/PycharmProjects/DemoQA1/screenshots/' + name_screenshot)