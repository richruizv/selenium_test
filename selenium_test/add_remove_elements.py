import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from pyvirtualdisplay import Display

class AddRemove(unittest.TestCase):

    def setUp(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        driver = self.driver
        self.driver.get('https://the-internet.herokuapp.com/add_remove_elements/')

        
        driver.implicitly_wait(10)

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add?'))
        elements_removed = int(input('How many elements will you remove?'))

        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_class_name('added-manually')
                delete_button.click()
            except:
                print('You are  trying to delete not existant')
                break
        if total_elements > 0:
            print(f'There are {total_elements} on elements ')


    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report'))