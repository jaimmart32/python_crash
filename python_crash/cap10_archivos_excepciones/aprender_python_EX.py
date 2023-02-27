# 10.1

filename = 'text_files/aprender_python.txt'

with open(filename) as file_o:
    content = file_o.read()
print(content)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_o:
    lines = file_o.readlines()

for line in lines:
    print(line.rstrip())

# 10.2

# replace() sustituye subcadenas en una cadena por la subcadena seleccionada.
print("************************************************************************)")
print(content.replace('Pedro', 'Perrrrrrro'))
print(content.replace('Python', 'C'))