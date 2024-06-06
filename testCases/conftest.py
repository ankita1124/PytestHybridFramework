from selenium import webdriver
import pytest




@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("-----------Launching Chrome Browser-----------")
        return driver
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("-----------Launching Firefox Browser-----------")
    else:
        driver=webdriver.Edge()
    return driver


def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

########## Pytest HTML Report ######################
# adding customized info to the report. It is a hook for adding environment into to HTML Report
def pytest_configure(config):
    config._metadata['Project Name']= "nop Commerce"
    config._metadata['Module Name']= "Customers"
    config._metadata['Tester']= "Ankita"

# It is hook for modifying/remove environment info from HTML repport
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins",None)

