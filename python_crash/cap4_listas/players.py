#PRINTING A SLICE OF A LIST

players = ['Messi','Maradona','Vieri','Pelé','Ronaldinho']
print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3:])
print('********************************************************************************************************************************')

# GO THROUGH A SLICE OF A LOOP

print("Aqui van los 3 primeros jugadores:")
for player in players[:3]:
    print(player.title())
