import unittest
from selenium import webdriver
from google_page import Google
from pyvirtualdisplay import Display
    

class GoogleTest(unittest.TestCase):

    @classmethod #Decoradores para correr en una sola instancia del navegador
    def setUpClass(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')


    def test_search(self):
        google = Google(self.driver)
        google.open()
        google.search('Python')

        self.assertEqual('Python', google.keyword)

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()