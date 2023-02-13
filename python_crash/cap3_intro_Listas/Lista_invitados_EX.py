# EJERCICIO 3.4

invitados = ['Marco Aurelio','Jose Dorronzoro','Tupac','Fredie Mercury']

for i in invitados:
    message = f"\nQuerido {i}, le informo de que ha sido invitado a la cena especial para indagar en los misterios del asado."
    print(message)
print("***********************************************************************************************************************")
# EJEERCICIO 3.5

no_assist = invitados.pop(2)
print(f"{no_assist} no podrá asistir, lo sentimos.\nPiense en otra persona por favor.")

invitados.insert(-1, 'Jesucristo')
for i in invitados:
    message = f"\nQuerido {i}, le informo de que ha sido invitado a la cena especial para indagar en los misterios del asado."
    print(message)
print("***********************************************************************************************************************")
# EJERCICIO 3.6

invitados = ['Marco Aurelio','Jose Dorronzoro','Tupac','Fredie Mercury']

for i in invitados:
    message = f"\nQuerido {i}, le informo de que se ha encontrado una mesa mas grande, habrá mas invitados."
    print(message)

invitados.insert(0,'Antonio Escohotado')
invitados.insert(2, 'Diogenes')
invitados.append('Nabucodonosor')

for i in invitados:
    message = f"\nQuerido {i}, le informo de que ha sido invitado a la cena especial para indagar en los misterios del pasado, version extendida."
    print(message)

print("***********************************************************************************************************************")
# EJERCICIO 7

invitados = ['Marco Aurelio','Jose Dorronzoro','Tupac','Fredie Mercury']

print("SOLO HAY ESPACIO PARA 2!")
j = 0
while len(invitados) > 2:
    not_invited = invitados.pop()
    print(f"Lo siento {not_invited}, ha ocurrido un percance y revocamos la invitación")
for i in invitados:
    print(f"\nQuerido {i}, le informamos de que sigue estando invitado, hay 2 plazas.")

del invitados[0]
del invitados[0]
print(invitados)