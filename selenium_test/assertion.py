import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pyvirtualdisplay import Display

class AssertionTest(unittest.TestCase):

    def setUp(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        driver = self.driver
        self.driver.get('http://demo-store.seleniumacademy.com/')

        driver.implicitly_wait(10)

    def testSearchField(self):
        self.assertTrue(self.isElementPresent(By.NAME,'q'))

    def testLanguageoption(self):
        self.assertTrue(self.isElementPresent(By.ID,'select-language'))

    def tearDown(self):
        self.driver.quit()
    
    def isElementPresent(self,how,what):
        try:
            self.driver.find_element(by= how, value = what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report'))