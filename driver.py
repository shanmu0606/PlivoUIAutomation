import unittest
from selenium import webdriver
import sys, os


class DriverManager(unittest.TestCase):
    """
    This class is for instantiating web driver instances.
    """

    def setUp(self):
        """
        This method is to instantiate the web driver instance.
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("http://quickfuseapps.com/")

    def tearDown(self):
        """
         To remove web driver object.
        """

        if self.driver is not None:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
