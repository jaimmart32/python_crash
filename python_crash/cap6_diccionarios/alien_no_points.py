#USAR get() PARA ACCEDER A VALORES

alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points'])

points_value = alien_0.get('points', 'No point value assigned.')
print(points_value)
