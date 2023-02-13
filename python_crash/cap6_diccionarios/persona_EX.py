persona = {'nombre': 'pablo', 'apellido': 'mora', 'edad': 30, 'ciudad': 'madrid'}
for key, value in persona.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


numeros_favoritos = {'deivid': '913523232', 'manu': '647147273', 'cela': '608183432',
 'mora': '675748393', 'arias': '656432546'}

for key, value in numeros_favoritos.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

glosario = {
    'parsing': 'Process of converting formatted text into a data structure.', 
    'logaritmo': 'Es una función que depende de una base y un argumento que crece a una tasa de crecimiento cada vez menor. Es la inversa de la función exponencial.',
    'varialble de entorno': 'Una variable de entorno es una variable dinámica que puede afectar al comportamiento de los procesos en ejecución en un ordenador. Son parte del entorno en el que se ejecuta un proceso.',
    'lógica': 'Ciencia formal que estudia los principios de la demostración y la inferencia válida,​ las falacias, las paradojas y la noción de verdad.​',
    'lenguaje de consulta': 'Un lenguaje de consulta es un lenguaje informático usado para hacer consultas en bases de datos y sistemas de información.'
    }
for key, value in glosario.items():
    print("·" + key + ":\n")
    print(value + "\n")

#EJERCICIO 6.7

persona_0 = {'nombre': 'jaime', 'apellido': 'cela', 'edad': 30, 'ciudad': 'madrid'}
persona_1 = {'nombre': 'laura', 'apellido': 'martinez', 'edad': 37, 'ciudad': 'san diego'} 

personas = [persona, persona_0, persona_1]

for pibe in personas:
    print(pibe)
print("********************************************************")

#EJERCICIO 6.8

mascota_1 = {'tipo': 'perro', 'dueño': 'jaime'}
mascota_2 = {'tipo': 'pez', 'dueño': 'cela'}
mascota_3 = {'tipo': 'gato', 'dueño': 'koke'}
mascota_4 = {'tipo': 'perro', 'dueño': 'arias'}

mascotas = [mascota_1, mascota_2, mascota_3, mascota_4]

for mascota in mascotas:
    print(f"{mascota['dueño'].title()} tiene un {mascota['tipo']}.")
print("**********************************************************")

#EJERCICIO 6.9

lugares_favoritos = {'jaime': ['granada', 'fuerteventura', 'cuenca'], 
'elena': ['granada', 'colombia', 'gante'], 'torrente': ['flowers', 'vibe', 'marbella'] }

for guy, lugares in lugares_favoritos.items():
    print(f"Nombre: {guy}")
    print(f"\nSus lugares favoritos son:\n")
    for sitio in lugares:
        print(sitio)
    print()
print("**********************************************************")

#EJERCICIO 6.10

persona = {'nombre': 'pablo', 'apellido': 'mora', 'edad': 30, 'ciudad': 'madrid'}
for key, value in persona.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


numeros_favoritos = {'deivid': '913523232', 'manu': '647147273', 'cela': '608183432',
 'mora': '675748393', 'arias': '656432546'}
numeros_favoritos_2 = {'ines': '91352542', 'casano': '645678273', 'inesluni': '635283432',
 'mora': '675748393', 'arias': '656432546'}
numeros_favoritos_3 = {'bové': '923453232', 'pepe': '647170873', 'cela': '608183432',
 'mora': '675748393', 'arias': '656432546'}
people = {
    'jaime': numeros_favoritos,
    'elena': numeros_favoritos_2,
    'chabo': numeros_favoritos_3,
    }

for persona, numeros in people.items():
    print(f"Los numeros favoritos de {persona.title()} son:")
    for contacto, telefono in numeros.items():
        print(f"{contacto.title()}: {telefono}")
    print()
