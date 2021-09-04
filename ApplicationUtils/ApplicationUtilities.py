import allure

from ApplicationUtils import configReader
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ApplicationUtilities:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locators):
        if str(locators).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", locators)).click()
        elif str(locators).endswith("_XPATH"):
            self.driver.find_element_by_css_selector(configReader.readConfig("locators", locators)).click()

    def WaitElement(self, driver):
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable)
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_selected)
        WebDriverWait(driver, 20).until(expected_conditions.frame_to_be_available_and_switch_to_it)

        #WebDriverWait(driver, 20).until(expected_conditions.frame_to_be_available_and_switch_to_it)
        #WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located(by.id())



