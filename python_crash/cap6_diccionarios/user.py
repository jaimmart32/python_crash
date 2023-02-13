#ITERAR EN BUCLE POR UN DICCIONARIO

#pasar en bucle por todos los pares clave-valor

user_0 = {
    'username': 'jaimmart',
    'first': 'jaime',
    'last': 'martinez',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    