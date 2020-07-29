import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: espanish or franch")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        if language == "es":
            print("\nchoosed spahish language...")
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
            browser = webdriver.Chrome(options=options)
        elif language == "fr":
            print("\nchoosed franch language...")
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
            browser = webdriver.Chrome(options=options)
        else:
            raise pytest.UsageError("--language_name should be spanish or franch")
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        if language == "es":
            print("\nchoosed spahish language...")
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", "es")
            browser = webdriver.Firefox(firefox_profile=fp)
        elif language == "fr":
            print("\nchoosed franch language...")
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", "fr")
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--language_name should be spanish or franch")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
