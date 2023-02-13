# RELLENAR UN DICCIONARIO CON ENTRADA DEL USUARIO

responses = {}

# Configura una bandera para indicar que la encuesta está activa.
polling_active = True

while polling_active:
    # Pide el nombre y la respuesta de la persona.
    name = input("\What is your name? ")
    response = input("Which mountain would you lije ti climb some day? ")

    # Guarda la respuesta en el diccionarío.
    responses[name] = response

    # Averigua si alguien más va a hacer la encuesta.
    repeat = input("Would you like to let another peson respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# La encuesta esta completa. Muestra los resultados.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")