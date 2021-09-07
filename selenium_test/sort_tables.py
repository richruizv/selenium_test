import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from pyvirtualdisplay import Display
from selenium.common.exceptions import NoSuchElementException

class SortTables(unittest.TestCase):

    def setUp(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        driver = self.driver
        self.driver.get('https://the-internet.herokuapp.com/tables')

        driver.implicitly_wait(10)

    def test_sort_tables(self):
        driver = self.driver
        table_data = []
        try:
            get_rows_table = driver.find_element_by_id('table1').get_property('rows')
            get_head_table = get_rows_table[0].get_property('cells')


            for i in range(1, len(get_rows_table)):
                data = {}
                for j in range(len(get_rows_table)):
                    get_head_cells = get_head_table[j].text
                    get_body_cells =  [i].get_property('cells')[j].text

                    data.update({get_head_cells:get_body_cells})
                table_data.append(data)

            print(table_data)
        except NoSuchElementException as ex:
            self.fail(ex.msg)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report'))