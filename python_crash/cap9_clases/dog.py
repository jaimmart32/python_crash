class Dog:
    """Un simple intento de modelare un perro."""
    def __init__(self, name, age):# self pasa automaticamente cuando se declare una instancia.
        """Inicializa los atributos de nombre y edad."""
        self.name = name# Atributo.
        self.age = age

    # Metodo sit
    def sit(self):
        """Simula un perro sentandose en respuesta a una orden."""
        print(f"{self.name} is now sitting.")
    
    # Metodo roll_over
    def roll_over(self):
        """Simula hacer la cocreta en respuesta a una orden."""
        print(f"{self.name} rolled over!")

# HACER UNA INSTANCIA DE UNA CLASE
my_dog = Dog('Greco', 4)

# Acceder a los atributos.
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Llamadas a métodos
my_dog.sit()
my_dog.roll_over()

# Crear múltiples instancias
your_dog = Dog('Nico', 8)

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()