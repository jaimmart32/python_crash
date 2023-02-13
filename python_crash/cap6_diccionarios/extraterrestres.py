#ANIDAR DICCIONARIOS EN UNA LISTA

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

extraterrestres = [alien_0, alien_1, alien_2]

for alien in extraterrestres:
    print(alien)

print("^*********************************************")

"""Usar range() para crear una flota de aliens."""

#Crea una lista vacia para guardar aliens.
aliens = []

# Crea 30 aliens verdes
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Muestra los primeros 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Muestra cuanrtos aliens se han creado.
print(f"Total number of aliens: {len(aliens)}")

print("**********************************************")

# Hace una lista vacia para guardar aliens.
aliens = []

# Hace 30 aliens verdes.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Cambia de color los 3 primeros aliens.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Muestra los 5 primeros aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
