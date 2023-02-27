#10.3

#name = input("Enter your name please: ")
#
#with open('text_files/invitado.txt', 'w') as file_obj:
#    file_obj.write(name)

# 10.4

names = []
while True:
    name = input("Enter your name: ")
    if name == "q":
        break
    names.append(name)
    print(f"Hi, {name}")
    with open('text_files/libro_invitados.txt', 'a') as file_o:
        file_o.write(name + "\n")
