# ESCRIBIR EN UN ARCHIVO

# escribir en un archivo vacio
filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love coding, specially in Python and C")


# escribir varias lineas

with open(filename, 'w') as file_object:
    file_object.write("I love coding, specially in Python and C.\n")
    file_object.write("I love creating games.\n")

# anexar a un archivo

with open(filename, 'a') as file_object:
    file_object.write("I love ma dog bro.\n")
    file_object.write("I love loving.\n")