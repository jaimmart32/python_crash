# EJERCICIO 7.8 Y 7.9

prompt = "\nDe que quieres el bocadillo? "
pedidos_bocadillos = []
bocadillos_terminados = []
active_pedido = 'no'
while True:
    bocata = input(prompt)
    pedidos_bocadillos.append(bocata)
    active_pedido = input("\nHas terminado tu pedido? (yes/ no)")
    if active_pedido == 'yes':
        break
if 'pastrami' in pedidos_bocadillos:
    print("\nLo siento pero no queda de pastrami.")
while 'pastrami' in pedidos_bocadillos:
    pedidos_bocadillos.remove('pastrami')
while pedidos_bocadillos:
        bocadillo = pedidos_bocadillos.pop()
        bocadillos_terminados.append(bocadillo)
        print(f"\n Su bocadillo de {bocadillo} está listo.")
print("\nEsta es la lista de los bocadillos listos:\n")
for bocata in bocadillos_terminados:
    print(f"bocadillo de {bocata}.")
