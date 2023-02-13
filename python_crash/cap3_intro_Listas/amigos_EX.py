# EJERCICIO 3.1

amigos = ["Arias","Manu", "Mora","Mario","Prado"]
for i in amigos:
    print(i)

# EJERCICIO 3.2

for i in amigos:
    msg = f"Que pasa, {i}."
    print(msg)

print()

# EJERCICIO 3.3

motos = ["Honda","Kawasaki", "Ducatti"]
for j in motos:
    msg = f"Me gustaria pilotar una {j}"
    msg1 = f"Las {j} son un pepino acho"
    msg2 = f"Las {j} suelen ser rojas"

    print(msg)
    print(msg1)
    if j == "Ducatti":
        print(msg2)