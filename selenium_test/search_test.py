import unittest
from selenium import webdriver
from pyvirtualdisplay import Display

class SearchTests(unittest.TestCase):

    def setUp(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        driver = self.driver
        self.driver.get('http://demo-store.seleniumacademy.com/')

        driver.implicitly_wait(10)
    
    def test_search_tee(self):
	    driver = self.driver
	    search_field = driver.find_element_by_name('q')
	    search_field.clear() #limpia el campo de búsqueda en caso de que haya algún texto. 
		
	    search_field.send_keys('tee') #simulamos la escritura del teclado para poner "tee"
	    search_field.submit() #envía los datos ('tee') para que la página muestre los resultados de "tee"

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.send_keys('salt shaker') #escribimos 'salt shaker' en la barra de búsqueda
        search_field.submit() #envíamos la petición

		#hago una lista de los resultados buscando los elementos por su Xpath. Es la forma más rápida.
        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')

		#vamos a preguntar si la cantidad de resultados es igual a 1
        self.assertEqual(1, len(products))
		
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report'))