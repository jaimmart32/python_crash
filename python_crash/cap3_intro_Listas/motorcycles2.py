motos = ['Honda','Derbi','suzuki']
print(motos)

motos[1] = 'Ducatti'
print(motos)

# APPEND AN ELEMENT AT THE LAST POSITION OF THE LIST
motos.append('Husqvarna')
print(motos)

coches = []

coches.append('BMW')
coches.append('Audi')
coches.append('Fiat')

print(coches)
print()

# INSERT AN ELEMENT IN AN ESPECIFIC POSITION
bugas = ['Mini', 'Renault']
bugas.insert(1,'Tesla')
print(bugas)

#   DELETE AN ELEMENT OF A LIST
del bugas[0]
print(bugas)

# DELETE AN ELEMENT WITH pop() SO WE CAN USE IT LATER
popped_car = bugas.pop()
print(bugas)
print(popped_car)
print()
# USE A POPPED ELEMENT
jugadores = ['Arias','Gala','Gontusso','Oski']
ultimo_en_tocar_el_palo = jugadores.pop()
print(f"Te la quedas de portero {ultimo_en_tocar_el_palo}.")
# POP A ESPECIFIC ELEMENT 
primero = jugadores.pop(0)
print(f"{primero} ha llegado primero.")
print()
# DELETE AN ELEMENT BY VALUE WITH remove()
partes = ['huevos','cara','nariz','boca']

partes.remove('cara')
print(partes)

motos = ['ducati','kawasaki','KTM']
print(motos)
# PRINT REASON FOR REMOVING WITH A VALUE NAME
muy_cara = 'ducati'
motos.remove(muy_cara)
print(motos)
print(f"\nUna {muy_cara.title()} es muy cara para mi.")

