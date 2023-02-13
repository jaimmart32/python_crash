class hero:
    def __init__(self, name, health, mana, lvl, rol):
        self.name = name
        self.health = health
        self.mana = mana
        self.lvl = lvl
        self.rol = rol

johanna = hero('Johanna', 4580, 113, 11,'tank')
li_li = hero('Li-li', 2800, 209, 9, 'healer')
valla = hero('Valla', 2300, 190, 8, 'ranged assasin')
varian = hero('Varian', 4300, 123, 12, 'melee assasin')
diablo = hero('Diablo', 5800, 205, 14, 'tank')
anduin = hero('Anduin', 2940,280, 10, 'healer')
raynor = hero('Raynor', 3400,292,14, 'ranged assasin')
illidan = hero('Illidan', 2200,0,10,'melee assasin')

print(johanna)
print(li_li)
print(valla)
print(varian)
print(diablo)
print(anduin)
print(raynor)
print(illidan)







