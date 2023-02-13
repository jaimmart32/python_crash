# PASAR UN NUMERO ARBITRARIO DE ARGUMENTOS

# * dice a python que cree una tupla vacia y meta ahi lo que reciba

def make_pizza(*toppings):
    """Resume la pizza que estamos a punto de hacer."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
