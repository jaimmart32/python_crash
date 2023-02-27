# 10.5

razones = []
while True:
    razon = input("Por que te gusta programar? ")
    if razon == "q":
        break
    razones.append(razon)
    with open('text_files/razones.txt', 'a') as file_obj:
        file_obj.write(razon + "\n")
