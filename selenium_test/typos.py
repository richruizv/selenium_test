import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from pyvirtualdisplay import Display

class Typos(unittest.TestCase):

    def setUp(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        driver = self.driver
        self.driver.get('https://the-internet.herokuapp.com/typos')

        driver.implicitly_wait(10)

    def test_find_typo(self):
        driver = self.driver
        text_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)').text
        tries = 1
        correct_text = "Sometimes you'll see a typo, other times you won't."
        while text_to_check != correct_text:
            text_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)').text
            tries += 1
            driver.refresh()
        print(f'It took {tries} tries to find the typo')
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report'))