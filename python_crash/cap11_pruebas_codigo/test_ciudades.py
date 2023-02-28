# 11.1 y 11.2

import unittest
from ciudad_funciones import get_city

class CityTestFormat(unittest.TestCase):
    """Pruebas para ciudad_funciones.py"""

    def test_ciudad_pais(self):
        """Funcionan las ciudades com 'Madrid' 'España'? """
        formatted_city = get_city('madrid', 'españa')
        self.assertEqual(formatted_city, 'Madrid, España')
    
    def test_ciudad_pais_habitantes(self):
        """Funcionan con parametro de población? """
        formatted_ciy = get_city('barcelona', 'españa', 4300546)
        self.assertEqual(formatted_ciy, 'Barcelona, España - habitantes 4300546')
    
if __name__ == '__main__':
    unittest.main()