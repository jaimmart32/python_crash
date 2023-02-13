alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#ACCEDER A LOS VALORES DEL DICCIONARIO

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#AÑADIR NUEVOS PARES CLAVE-VALOR

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#EMPEZAR CON UN DICCIONARIO VACIO

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#MODIFICAR VALORES EN UN DICCIONARIO

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")



alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x_position: {alien_0['x_position']}")
# Mueve el alien hacia la derecha.
# Determina cúanto se mueve el alien basandose en su velocidad actual.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Debe ser un alien rápido
    x_increment = 3

# La nueva posición es la antigua mas el incremento.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x_position: {alien_0['x_position']}")

alien_0['speed'] = 'fast'

#ELIMINAR PARES DE VALOR

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
