
"""Una clase que se puede usar para representar un coche."""

class Car:
    """Intento de representar un coche."""

    def __init__(self, make, model, year):
        """Inicializa los atributos para describir un coche."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Establecer un valor predeterminado para un atributo
    

    def get_descriptive_name(self):
        """"Devuelve un nombre descriptivo con el formato adecuado."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    

    def read_odometer(self):
        """IMprime una oración que indica el kilometraje del coche."""
        print(f"This car has {self.odometer_reading}km on it.")
    

    # Modificar atributo traves de un metodo
    def update_odometer(self, kilometraje):
        """Configura el kilometraje con el valor dado.
        Rechaza el cambio si se intenta hacer retroceder el cuentakilometros."""
        if kilometraje >= self.odometer_reading:
            self.odometer_reading = kilometraje
        else:
            print("You can't roll back an odometer, bad boy!")
    

    # Aumentar el valor de un atributo a través de un método
    def increment_odometer(self, km):
        """Añade la cantidad dada a la lectura del cuentakilometros."""
        if km > 0:
            self.odometer_reading += km


# Aumentar a traves de método
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(10_000)
my_used_car.read_odometer()

my_used_car.increment_odometer(150)
my_used_car.read_odometer()