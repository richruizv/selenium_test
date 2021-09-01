from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner #para generar el reporte
from assertion import AssertionTest
from search_test import SearchTests


assertions_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

#contruimos la suite de pruebas
smoke_test = TestSuite([assertions_test, search_tests])


#para generar los reporters
kwargs = {
    "output": 'smoke-report'
    }

#la variable runner almacena un reporte generado por HTMLTestRuner
#usa como argumento "kwarsp"
runner = HTMLTestRunner(**kwargs)

#corro el rurner con la suite de prueba
runner.run(smoke_test) 