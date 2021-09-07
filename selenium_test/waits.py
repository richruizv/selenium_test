import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#Herramienta para hacer uso de las expected conditions y esperas explicitas
from selenium.webdriver.support.ui import WebDriverWait

#Importar esperar explicitas
from selenium.webdriver.support import expected_conditions as EC



class Waits(unittest.TestCase):

    time = 5
    create_time = 5

    def setUp(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.implicitly_wait(10)

    def test_account_link(self): #Cuentas del sitio

        #Esperar 10 segundos hasta que se cumpla la funcion
        WebDriverWait(self.driver, self.time).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')  
        print('Wait 3 secs')
        #Hacer referencia al enlace donde estan las cuentas
        account = WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        print('Wait another 3 secs')
        account.click()

    def test_create_new_customer(self): #Creacion de nuevo usuario

        #Encontrar el elemento por el texto del enlace
        self.driver.find_element_by_link_text('ACCOUNT').click()
        #Hacer referencia a la cuenta
        my_account = WebDriverWait(self.driver, self.create_time).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        #Referencia a crear una cuenta
        create_account = WebDriverWait(self.driver, self.create_time).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account.click()

        #Verificacion de estado de pagina web
        WebDriverWait(self.driver, self.create_time).until(EC.title_contains('Create New Customer Account'))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report'))