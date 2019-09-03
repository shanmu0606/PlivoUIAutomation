import unittest
from selenium import webdriver
import time
from common_methods import Common
from driver import DriverManager

class MyTestCase(DriverManager):
    """
    Test method to create an app
    drag and drop SMS messaging
    """
    def test_createapp(self):
        common = Common(self.driver)
        common.createapp_page()
        common.drag_and_drop()

if __name__ == '__main__':
    unittest.main()
