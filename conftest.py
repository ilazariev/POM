
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', default='en', help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstarting chrome browser for test...")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.headless = True
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquitting browser...")
    browser.quit()
