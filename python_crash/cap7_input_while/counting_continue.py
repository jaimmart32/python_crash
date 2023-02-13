# USAR continue EN UN BUCLE
# continue vuelve al principio del bucle si se cumple una condicion ignoran el codigo posterior
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
