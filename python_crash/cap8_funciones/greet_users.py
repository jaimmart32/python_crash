# PASAR UNA LISTA

def greet_users(names):
    """Imprime un saludo sencillo para cada usuario de la lista."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['mora', 'prado', 'cela', 'arias', 'manu']
greet_users(usernames)