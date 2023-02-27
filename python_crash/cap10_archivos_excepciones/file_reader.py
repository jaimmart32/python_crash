# LEER DE UN ARCHIVO COMPLETO

# asignar ruta absoluta del archivo a la variable file_path.
file_path = '/home/jaimmart32/Desktop/python_crash/python_crash/cap10_archivos_excepciones/text_files/pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
print(contents)
# rstrip()elimina cualquier caracter blanco a la derecha de una cadena.
print(contents.rstrip())

# Leer linea por linea de un archivo
file_name = 'text_files/pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# HACER UNA LISTA DE LINEAS DE UN ARCHIVO

with open(file_name) as file_o:
    lines = file_o.readlines()

for line in lines:
    print(line.rstrip())
