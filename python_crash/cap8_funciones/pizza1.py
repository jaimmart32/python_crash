# MEZCLAR ARGUMENTOS POSICIONALES Y ARBITRARIOS

def make_pizzas(size, *toppings):
    """Resume la pizza que estamos a punto de hacer."""
    print(f"\nMaking a {size}-cm pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizzas(16, 'peperoni')
make_pizzas(12, 'mushrooms', 'green peppers', 'extra cheese')