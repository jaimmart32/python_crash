# 10.8 y 10.9

gatos = 'text_files/gatos.txt'
perros = 'text_files/perros.txt'
filename = gatos
try:
    with open(filename) as f:
        lst_file = f.readlines()
    for name in lst_file:
        print(name)
except FileNotFoundError:
    pass
