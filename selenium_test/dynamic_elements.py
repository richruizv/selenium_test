import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from pyvirtualdisplay import Display

class DynamicElements(unittest.TestCase):

    def setUp(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        driver = self.driver
        self.driver.get('https://the-internet.herokuapp.com/disappearing_elements')

        driver.implicitly_wait(10)
    
    def test_name_elements(self):
        driver = self.driver

        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option number {i + 1} is NOT FOUND")
                    tries+=1
                    driver.refresh()
        
        print(f'Finished in {tries} tries')


    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report'))