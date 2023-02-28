# 11.3

import unittest
from empleado import Empleado

class TestEmpleado(unittest.TestCase):
    """Prueba que la clase Empleado funciona como se espera."""

    def setUp(self):
        """Crea una instancia de Empleado para usar en todos los métodos de prueba."""
        self.mi_empleado = Empleado('juanchu', 'marina', 21000)
    
    def test_dar_aumento_predeterminado(self):
        """Comprueba que dar_aumento() funciona correctamente con valor predeterminado."""
        self.mi_empleado.dar_aumento()
        self.assertEqual(self.mi_empleado.salario_anual, 26000)
    
    def test_dar_aumento_personalizado(self):
        """Comprueba que dar_aumento() funciona con un valor personalizado."""
        self.mi_empleado.dar_aumento(32)
        self.assertEqual(self.mi_empleado.salario_anual, 21032)

if __name__ == '__main__':
    unittest.main()
