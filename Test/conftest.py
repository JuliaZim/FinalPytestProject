from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import FirefoxProfile


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    link = "http://selenium1py.pythonanywhere.com/"
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FirefoxProfile()
        options.set_preference("intl.accept_languages", language)
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        browser = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()

