import allure
import pytest
from allure_commons.types import AttachmentType

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ApplicationUtils import configReader
@pytest.fixture(params=["chrome"],scope="function")
def get_browser(request):
    global driver
    if request.param=="chrome":
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())

    if request.param=="firefox":
        driver=webdriver.Firefox(executable_path=GeckoDriverManager.install())

    request.cls.driver=driver
    driver.get(configReader.readConfig("basic_info", "testsiteurl"))
    driver.maximize_window()
    driver.implicitly_wait(1)
    yield driver
    driver.quit

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
        print("11111111111111111111111111111111111111111")

        outcome=yield
        rep=outcome.get_result()
        setattr(item, "rep_"+rep.when, rep)
        return rep


@pytest.fixture()
def log_on_failure(request):
    print("***************************************************************")
    yield
    item=request.node
    if item.rep_call.failed:
        allure.attach(request.driver.get_screenshot_as_png(), name="/ApplicationReports",attachment_type=AttachmentType.PNG)
