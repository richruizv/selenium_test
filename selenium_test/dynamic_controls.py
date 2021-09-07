import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from pyvirtualdisplay import Display

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicControls(unittest.TestCase):

    def setUp(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        driver = self.driver
        self.driver.get('https://the-internet.herokuapp.com/dynamic_controls')

        driver.implicitly_wait(10)
    
    def test_dynamic_controls(self):

        driver = self.driver 
        
        driver.find_element_by_css_selector("#checkbox > input[type=checkbox]")
        remove_add_button = driver.find_element_by_css_selector("#checkbox-example > button")
        remove_add_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#checkbox > input[type=checkbox]")))
        remove_add_button.click()

        # we wait for the button

        enable_disable_button = driver.find_element_by_css_selector("#input-example > button")
        enable_disable_button.click()

        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button")))
        
        text_area = driver.find_element_by_css_selector("#input-example > input[type=text]")
        text_area.send_keys('Platzi')

        enable_disable_button.click()
      
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report'))