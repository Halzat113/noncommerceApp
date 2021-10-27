import pytest
from selenium import webdriver

from utilities.readProperties import ReadConfig

baseUrl = ReadConfig.getApplicationCredential("baseUrl")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseUrl)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


##################  Pytest HTML Report #####################

# It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Non Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Halzat'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

    # pytest -v  --capture=tee-sys --html=Reports\report.html testCases/test_login.py --browser chrome (using
    # terminal to run test and get the result)
