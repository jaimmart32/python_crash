#EJERCICIO 4.10

hots_heroes = ['Valla', 'Diablo', 'Tracer', 'Sonya', 'Garrosh', 'Muradin', 'Kharazim']

print("Estos son los 3 primeros elementos de la lista:")
print(hots_heroes[:3])

print("Estos son los 3 elementos de en medio:")
print(hots_heroes[2:5])

print("Estos son los 3 últimos elementos de la lista")
print(hots_heroes[4:])

print("\n***************************************************************")

#EJERCICIO 4.11

pizzas = ['diavola','cuatro quesos','parmiggiana','barbacoa']
friends_pizzas = pizzas[:]

pizzas.append('Hawaiana')
friends_pizzas.append('Nutella')

print("Mis pizzas favoritas son:")
for pizza in pizzas:
    print("· " + pizza)

print("\n")

print("Las pizzas favoritas de mi colega son:")
for f_pizza in friends_pizzas:
    print("· " +  f_pizza)

#EJERCICIO 4.12

my_foods = ['pizza', 'falafel', 'carrot cake']

friends_foods = my_foods[:] 

my_foods.append('cogollos')
friends_foods.append('Ice cream')
print("Mi favorite foods are:")
for food in my_foods:
    print("· " + food)

print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print("· " + food)

print("\n**************************************************************")

#EJERCICIO 4.13

basic_food = ('pasta', 'huevos', 'carne', 'pescado', 'ensalada')
for food in basic_food:
    print(food)
#basic_food[3] = 'pene'
print()

basic_food = ('pasta', 'huevos', 'ass', 'pussy', 'ensalada')
for food in basic_food:
    print(food)

#EJERCICIO 4.14

# https://python.org/dev/peps/pep-0008/

#EJERCICIO 4.15

