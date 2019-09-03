from selenium import webdriver
from services import Services
from selenium.webdriver.common.action_chains import ActionChains
import time
class Common():

    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.createapp_xpath = '// *[ @ id = "link-create"]'
        self.start_xpath = '//*[@id="intro-dialog-cont"]/div[2]/button'
        self.newpage_xpath = '//*[@id="add-page"]'
        self.entername_xpath = '//*[@id="create-dialog"]/form/p/input'
        self.text = "TEST"
        self.createbutton_xpath = '/html/body/div[20]/div[3]/button[1]'
        self.clicknewpage_xpath = '//*[@id="accordion"]/h3[4]/a'


    def createapp_page(self):
        """
        This method is used to create app
        Create a new page and give a new name to it
        :return:
        """
        self.services.wait_for_element(self.createapp_xpath)
        self.driver.find_element_by_xpath(self.createapp_xpath).click()
        self.driver.implicitly_wait(5)


        self.driver.find_element_by_xpath(self.start_xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.newpage_xpath).click()
        name = self.driver.find_element_by_xpath(self.entername_xpath)
        name.click()

        self.driver.implicitly_wait(50)
        name.send_keys(self.text)
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[20]/div[3]/button[1]').click()


        self.driver.find_element_by_xpath(self.clicknewpage_xpath).click()

    def drag_and_drop(self):

        source_element = self.driver.find_element_by_xpath('//*[@id="accordion"]/div[4]/ul/li[3]')
        time.sleep(5)
        dest_element = self.driver.find_element_by_xpath('//*[@id="tabs-2"]')
        ActionChains(self.driver).drag_and_drop(source_element, dest_element).perform()
        time.sleep(5)

        # drag and drop arrow to destination
        #source_element = self.driver.find_element_by_xpath('//*[@id="node-517670"]')
        #dest_element = self.driver.find_element_by_xpath('//*[ @id="rec-276256"]')


