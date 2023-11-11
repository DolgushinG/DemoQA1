import time
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as CromeOptions

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from constants import OUTPUT_ROOT


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox or edge")


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    # chrome_options = webdriver.ChromeOptions
    # chrome_options.page_load_strategy = "eager" #браузер работает моментально
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox or edge")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield request.cls.driver
    request.cls.driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.originalname)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.cls.driver
            take_screenshot(driver, request.node.originalname)
            print("executing test failed", request.node.originalname)


def take_screenshot(driver, originalname):
    time.sleep(1)
    file_name = \
        f'{originalname}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
    driver.save_screenshot(f"{OUTPUT_ROOT}/{file_name}")
    allure.attach(driver.get_screenshot_as_png(),
                  name=f"{OUTPUT_ROOT}/{file_name}",
                  attachment_type=allure.attachment_type.PNG)



