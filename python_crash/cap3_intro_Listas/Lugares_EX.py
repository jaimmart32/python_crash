# EJERCICIO 3.8

lugares = ['Thailandia', 'California', 'Rumanía']
print(lugares)
print(sorted(lugares))
print(lugares,"\n")

print(sorted(lugares,reverse=True))
print(lugares,"\n")

lugares.reverse()
print(lugares,"\n")
lugares.reverse()
print(lugares,"\n")

lugares.sort()
print(lugares)

lugares.sort(reverse=True)
print(lugares)

print("***************************************************************************************************************\n")
# EJERCICIO 3.9

invitados = ['Marco Aurelio','Jose Dorronzoro','Tupac','Fredie Mercury']

for i in invitados:
    message = f"\nQuerido {i}, le informo de que ha sido invitado a la cena especial para indagar en los misterios del asado."
    print(message)
print(f"\n{len(invitados)} personas han sido invitadas a la cena.")

print("***************************************************************************************************************\n")
#EJERCICIO 3.10 todas las funciones del capitulo en una lista que contenga idiomas


# EJERCICIO 3. 11 eRROR INTENCIONADO

lenguas = ['Español','Italiano','Rumano','Ingles']
# print(lenguas[4]) list index out of range error
print(lenguas[3])


