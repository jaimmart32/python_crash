#EJERCICIO 5.3

color_alien = 'verde'

if color_alien == 'verde':
    print("+5 points!")

color_alien = 'rojo'

if color_alien == 'verde':
    print("+5 points!")

print("*************************************************")

#EJERCICIO 5.4

color_alien = 'amarillo'

if color_alien == 'verde':
    print("+5 points!")
else:
    print("+10 points!")

color_alien = 'verde'

if color_alien == 'verde':
    print("+5 points!")
else:
    print("+10 points!")

print("\n**************************************************")

#EJERCICIO 5.5

color_alien = 'rojo'

if color_alien == 'verde':
    print("+5 points!")
elif color_alien == 'amarillo':
    print("+10 points!")
elif color_alien == 'rojo':
    print("+15 points!")

print("\n**************************************************")

#EJERCICIO 5.6

edad = 30

if edad < 2:
    print("Eres un bebé!")
elif edad < 4:
    print("Eres un infante!")
elif edad < 13:
    print("Eres un niño!")
elif edad < 20:
    print("Eres un adolescente!")
elif edad < 65:
    print("Eres un adulto!")
else:
    print("Eres un anciano!")

print("\n**************************************************")

#EJERCICIO 5.7

frutas_favoritas = ['mango', 'papaya', 'sandía']
if 'piña' in frutas_favoritas:
    print("Pues si que te gustan las piñas!")
if 'papaya' in frutas_favoritas:
    print("Pues si que te gustan las papayas!")
if 'sandía' in frutas_favoritas:
    print("Pues si que te gustan las sandías!")
if 'manzana' in frutas_favoritas:
    print("Pues si que te gustan las manzanas!")
if 'pera' in frutas_favoritas:
    print("Pues si que te gustan las peras!")