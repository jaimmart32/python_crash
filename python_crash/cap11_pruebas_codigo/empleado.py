# 11.3

class Empleado:
    """Intento de representar un empleado."""

    def __init__(self, nombre, apellido, salario_anual):
        """Guarda los atributos de un empleado."""
        self.nombre = nombre
        self.apellido = apellido
        self.salario_anual = salario_anual
    
    def dar_aumento(self, aumento=5000):
        """Da un aumento de suedldo de 5000 euros a un empleado."""
        self.salario_anual += aumento

