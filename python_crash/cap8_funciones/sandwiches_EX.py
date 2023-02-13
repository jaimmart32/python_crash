# 8.12

def print_sandwiches(*sandwiches):
    for sandwich in sandwiches:
        print(f"\nPidiendo un sandwich: {sandwich.title()}")

print_sandwiches('mixto')
print_sandwiches('rucula', 'chorizo', 'serrano')
print_sandwiches('nutella', 'queso')

# 8.13

def build_profile(first, last, **user_info):
    """Crea un diccionario con todo lo que sabemos sobre un usuario."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('jaime', 'martinez',
                             location='madrid',
                             field='sage',
                             power=100)
print(user_profile)

print("***************************************************************************************************")
#8.14

def create_car(marca, modelo, **car_info):
    """Crea un diccionario con todo lo que sabemos sobre un coche."""
    car_info['fabricante'] = marca.title()
    car_info['modelo'] = modelo.title()
    return car_info

car_profile = create_car('lamborgini', 'murcielago',
                             power='533hp',
                             puertas=2,
                             color='yellow')
print(car_profile)