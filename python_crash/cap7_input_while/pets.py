# ELIMINAR TODOS LOS CASOS DE VALORES ESPECIFICOS DE UNA LISTA

pets = ['dog', 'cat', 'dog', 'cat', 'goldfish', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
