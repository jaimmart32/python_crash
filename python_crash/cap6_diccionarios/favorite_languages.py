#DICCIONARIO DE OBJETOS SIMILARES

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'mora': 'ruby',
    'jimmy': 'python',
}

language = favorite_languages['jimmy'].title()
print(f"Jimmy's favorite language is {language}.")
print("**************************************************************")

#iterar en bucle por todos los pares clave-valor

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("***************************************************************")


#iterar en bucle por todas las claves

for name in favorite_languages.keys():
    print(name.title())
# o

for name in favorite_languages:
    print(name.title())  
print("****************************************************************")

friends = ['jimmy', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
        

#averiguar si existe una clave

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("****************************************************************")

#iterar por las claves de un diccionario en un orden en particular

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
print("****************************************************************")

#iterar por todos los valores de un diccionario values()

print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())

print("***************************************************************+")

#set() para evitar repeticion de valores

print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(language.title())
print("****************************************************************")

# LISTAS EN LAS CLAVES DE UN DICCIONARIO

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
        
    