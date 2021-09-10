import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from pyvirtualdisplay import Display

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ProjectMercadolibre(unittest.TestCase):

    time = 10

    def setUp(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        self.driver.get('http://mercadolibre.com')
        self.driver.implicitly_wait(10)
    
    def test_page(self):
        driver = self.driver
        colombia = driver.find_element_by_id('CO')
        colombia.click()
        self.assertEqual('https://www.mercadolibre.com.co/#from=homecom',driver.current_url)
        
        # simulating the search of playstation
        search_field = driver.find_element_by_name('as_word')
        search_field.clear() 
        search_field.send_keys('Playstation 5') 
        search_field.submit()
        
        #filter by new products
        sleep(3)
        new = driver.find_element_by_css_selector('a[aria-label="Nuevo"]')
        driver.execute_script("arguments[0].click();", new)
        #We need explicit wait to expect the load of other pages
        

        #filtering products by location, which is bogota
        sleep(3)
        bogota = driver.find_element_by_css_selector('a[aria-label="Bogotá D.C."]')
        driver.execute_script("arguments[0].click();", bogota)

        order_menu=driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > button')
        order_menu.click()
        value=driver.find_element_by_partial_link_text('Mayor precio')
        driver.execute_script("arguments[0].click();", value)
        sleep(3)
        
        article_name =  driver.find_elements_by_class_name('ui-search-item__title')
        price = driver.find_elements_by_class_name('price-tag-fraction')
        
        objects = []
        for i in range(5):
            objects.append({'article_name' : article_name[i].text,'price': price[i].text})
            #objects[article_name] = price
        
        print(objects)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report'))