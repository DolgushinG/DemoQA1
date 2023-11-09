from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# def get_options(browser_name: str) -> Any:
#     if browser_name == 'chrome':
#         chrome_options = ChromeOptions()
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-gpu")
#         chrome_options.add_argument("--disable-extensions")
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--start-maximized")
#         #chrome_options.page_load_strategy = "eager"
#         return chrome_options