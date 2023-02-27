# GUARDAR Y LEER DATOS GENERADOS POR USUARIOS

# REFACTORIZACION

import json

# Carga el nombre de usuario si se ha guardado previamente.
# Si no es el caso, solicita el nombre de usuario y lo guarda

def get_stored_username():
    """Obtiene un nombre de usuario almacenado si esta disponible."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Solicita un nuevo nombre de usuario."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Saluda al usuario por su nombre."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when yyou come back, {username}!")


greet_user()
