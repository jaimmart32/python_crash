# UAN PRUEBA QUE PASA

import unittest
from name_function import get_formatted_name

# unittest.TestCase incluye varios metodos assert para compbrobar el output de funciones y clases.
class NamesTestCase(unittest.TestCase):
    """Pruebas para 'name_function.py'."""

    def test_first_last_name(self):
        """Funcionan nombres como 'Janis Joplin'?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        # Los metodos assert() comprueban que el resultado recibido coincide con el resultado esperado.
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_middle_last_name(self):
        """Funcionan los nombres compuestos?"""
        formatted_name =get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

# Buscala variable especial __name__ , que se establece cuando se ejecuta el programa.
# Si este archivo se ejecuta como programa principal y no como MODULO el valor de __name__ sera __main__
# En este caso llamamos a unittest.main(), que ejecuta el caso de prueba.
if __name__ == '__main__':
    unittest.main()