import allure
from pages.practice_form_page import PracticeFormPage
from pages.main_page import MainPage
from pages.forms_page import FormsPage
#from constants import DATA_ROOT1
import time
import pytest
from generator.generator import generate_person


class TestForm:
    def test_form1(self, browser):
        person = generate_person()
        practice_form_page = PracticeFormPage(browser)
        practice_form_page.open('https://demoqa.com/automation-practice-form')
        practice_form_page.fill_in_fist_name(person.first_name)
        practice_form_page.fill_in_last_name(person.last_name)
        practice_form_page.fill_in_email(person.email)
        practice_form_page.select_male_radiobutton()
        practice_form_page.fill_in_number(person.mobile)
        practice_form_page.open_birth_date_window()
        practice_form_page.open_year_list()
        practice_form_page.select_year()
        practice_form_page.select_date()
        practice_form_page.scroll_down()
        practice_form_page.fill_in_subject("e")
        practice_form_page.select_subject()
        practice_form_page.select_sports_radiobatton()
        # file1 = DATA_ROOT1
        practice_form_page.add_picture('/Users/sasha17/PycharmProjects/DemoQA1/data/ship.jpg')
        practice_form_page.fill_in_adress(person.address)
        practice_form_page.remove_footer()
        practice_form_page.open_state_list()
        practice_form_page.select_state()
        practice_form_page.open_city_list()
        practice_form_page.select_city()
        practice_form_page.click_submit()
        practice_form_page.check_modal_email(person.email)
        practice_form_page.check_phone_number(person.mobile)
        #practice_form_page.check_address(person.address)
        practice_form_page.check_gender()
        time.sleep(2)
        practice_form_page.take_screenshot()

    @allure.epic("Форма")
    @allure.feature("Открытие формы")
    @allure.story("Видимость")
    @allure.title("Проверка открытия страницы с формой")
    def test_form2(self, browser):
        main_page = MainPage(browser)
        forms_page = FormsPage(browser)
        practice_form_page = PracticeFormPage(browser)

        main_page.open("https://demoqa.com/")
        main_page.scroll_down()
        main_page.click_main_btn_forms()
        forms_page.click_practice_form()
        practice_form_page.fill_in_fist_name("das")
        practice_form_page.fill_in_last_name("dasd")








