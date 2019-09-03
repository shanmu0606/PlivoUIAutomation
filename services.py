from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Services:
    def __init__(self, driver):
        self.driver = driver

    def click_by_xpath(self, locator):
        """
        This method is to assert and click on the web element.
        param locator: XPATH of given element
        param_type: string
        """

        self.wait_for_element(locator)
        ele = self.driver.find_element_by_xpath(locator)
        ele.click()

    def wait_for_element(self, locator, timeout=20):

        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))

    def get_text_by_xpath(self, locator):
        """
        This method is get the text present within given web element.
        param locator: XPATH of given element
        param_type: string
        """

        return self.driver.find_element_by_xpath(locator).text
