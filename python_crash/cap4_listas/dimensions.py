# DEFINIR UNA TUPLA. Una lista inmutable es una Tupla.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 32  da error pues una tupla es inmutable

#para crear una tupla de un elemento hay que incluir una coma
mi_tupla = (3,)

#ITERAR CON UN BUCLE LOS VALORES DE UNA TUPLA

for dimension in dimensions:
    print(dimension)

#SOBRESCRIBIR UNA TUPLA
#Aunque no se puede modificar una tupla, si se puede asignar un valor a una variable que representa una tupla.

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 20)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

