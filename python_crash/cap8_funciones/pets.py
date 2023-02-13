# PASAR ARGUMENTOS

# Argumentos posicionales

def describe_pet(animal_type, pet_name):
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}' s name is {pet_name.title()}.")

describe_pet('owl', 'harry')
describe_pet('dog', 'greco')

# Argumentos de palabra clave

describe_pet(animal_type='cat', pet_name='cleo')# El orden de los argumentos es indiferente con argumentos de palabra clave.

# Valores predeterminados

def describe_pet(pet_name, animal_type='dog'):# Si no se indica animal_type, por defecto sera dog.
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}' s name is {pet_name.title()}.")