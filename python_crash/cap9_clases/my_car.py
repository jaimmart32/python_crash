# IMPORTAR VARIAS CLASES DE UN MODULO
from car import Car
from electric_car import ElectricCar

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# MODIFICAR EL VALOR DE UN ATRIBUTO

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# A traves de metodo
my_new_car.update_odometer(430)
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'roadster', 2021)
print(my_tesla.get_descriptive_name())