# HERENCIA
"""La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, 
compartiendo sus métodos y atributos. Además de ello, una clase hija puede sobreescribir los métodos o atributos, 
o incluso definir unos nuevos. Se puede crear una clase hija con tan solo pasar como parámetro la clase de la que queremos heredar."""

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


# INSTANCIAS COMO ATRIBUTOS
# Podemos descomponer una clase grande en varias pequeñas juntas.
class Battery:
    """Intento de modelar una batería para un coche eléctrico."""

    def __init__(self, battery_size=75):
        """Inicializa los atributos de la batería."""
        self.battery_size = battery_size
    

    def describe_battery(self):
        """Imprime una frase que describe el tamaño de la batería."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    

    def get_range(self):
        """Imprime una frase sobre la autonomía que ofrece esta batería."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} km on a full charge.")
        
# La función super() permite llamar un metodo de la clase base/madre.
class ElectricCar(Car):
    """Representa aspectos de un coche propios de los vehiculos eléctricos."""

    def __init__(self, make, model, year):
        """Inicializa los atributos base de la clase base/madre/superclase.
        Luego inicializa los atributos específicos de un coche eléctricomediante la instancia Battery()."""
        super().__init__(make, model, year)
        # Definir atributos especificos de la clase derivada
        self.battery = Battery() # Instancia como atributo
    

    #def describe_battery(self):
    #    """Imprime una frase que describe el tamaño de la batería."""
    #    print(f"This car has a {self.battery_size}-kWh battery.")
    

    # Anular metodos de la clase base(si se llama a fill_gas tank con un coche eléctrico, 
    # python ignorará el método de Car y ejecutará el de ElectricCar)
    def fill_gas_tank(self):
        """Los coches eléctricos no tienen gasolina y por lo tanto depósito."""
        print("This car doesn't need a gas tank.")


my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # acceder al metodo describe_battery() que esta dentro de la subclase(atributo de clase
                                    # ElectricCar) Battery que a su vez esta dentro de la instancia my_tesla(ElectricCar). 

my_tesla.battery.get_range()