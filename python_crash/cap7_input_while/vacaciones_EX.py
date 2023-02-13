# EJERCICIO 7.10

prompt = "¿Si pudieras visitar cualquier sitio que sitio seria? "

responses = {}

# Configura una bandera para indicar que la encuesta está activa.
polling_active = True

while polling_active:
    # Pide el nombre y la respuesta de la persona.
    name = input("\nWhat is your name? ")
    response = input(prompt)

    # Guarda la respuesta en el diccionarío.
    responses[name] = response

    # Averigua si alguien más va a hacer la encuesta.
    repeat = input("Would you like to let another peson respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# La encuesta esta completa. Muestra los resultados.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to go on vacation to {response.title()}")