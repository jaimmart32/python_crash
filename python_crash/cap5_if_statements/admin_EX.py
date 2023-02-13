#EJERCICIO 5.8

usuarios = ['jaime','elena','laura','inma','admin']

for usuario in usuarios:
    if usuario == 'admin':
        print("Hola admin, quiere ver un informe de estado?")
    else:
        print(f"Hola {usuario}, nos vemos de nuevo!")

print("**************************************************************")

#EJERCICIO 5.9

usuarios = []
if usuarios:
    for usuario in usuarios:
    
        if usuario == 'admin':
            print("Hola admin, quiere ver un informe de estado?")
        else:
            print(f"Hola {usuario}, nos vemos de nuevo!")
else:
    print("¡Necesitamos encontrar un usuario!")

print("**************************************************************")

#EJERCICIO 5.10

current_ussers = ['jaime','elena','laura','inma','juan']
new_ussers = ['joaquin','milena','Laura','inma','pedro']

for usser in new_ussers:
    if usser.lower() in current_ussers:
        print("This ussername has already been chosen, try another!")
    else:
        print("This ussername is available!")

print("**************************************************************")

#EJERCICIO 5.11

numbers = [1,2,3,4,5,6,7,8,9]

for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
    