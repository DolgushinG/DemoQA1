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





def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox or edge")


@pytest.fixture()
def browser(request):
    # chrome_options = webdriver.ChromeOptions
    # chrome_options.page_load_strategy = "eager" #браузер работает моментально
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name =="edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox or edge")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_1(browser):
    browser.get("https://demoqa.com/")
    browser.execute_script("window.scrollTo(0, 200)")
    browser.find_element(By.XPATH, "//*[text() = 'Forms']").click()
    browser.save_screenshot('screenshot.png')