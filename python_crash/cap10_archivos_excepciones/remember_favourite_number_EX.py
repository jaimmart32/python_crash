# 10.12

import json

def get_stored_f_number():
    """Obtiene un numero favorito almacenado si esta disponible."""
    filename = 'favourite_numbers.json'
    try:
        with open(filename) as f:
            f_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return f_number
    
def get_new_f_number():
    """Solicita un nuevo numero favorito."""
    f_number = input("What is your favourite number? ")
    filename = 'favourite_numbers.json'
    with open(filename, 'w') as f:
        json.dump(f_number, f)
    return f_number

def show_fav_number():
    """Imprime el numero favorito si esta, si no lo almacena."""
    f_number = get_stored_f_number()
    if f_number:
        print(f"Your favourite number is {f_number}!")
    else:
        f_number = get_new_f_number()
        print(f"We'll remember your favourite number: {f_number} when you come back!")


show_fav_number()