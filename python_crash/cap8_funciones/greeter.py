# PASAR INFORMACION A UNA FUNCION(parámetros(username) y argumentos('jesse'))

def greet_user(username):
    """Muestra un simple saludo"""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

# USAR UNA FUNCION CON UN BUCLE WHILE

def get_formatted_name(first_name, last_name):
    """Devuelve un nombre completo, con un formato adecuado."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")