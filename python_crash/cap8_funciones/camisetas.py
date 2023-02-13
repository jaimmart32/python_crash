# EJERCICIO 8.3 y 8.4

def hacer_camiseta(talla='XL', mensaje='I love python'):
    print(f"Camiseta talla {talla}, con el mensaje impreso: '{mensaje}'.")

hacer_camiseta('M', 'return NULL to the matrix')
hacer_camiseta(mensaje='liberalismo rules', talla='S')

hacer_camiseta(talla='M')
hacer_camiseta(talla='S', mensaje='cacota')

# EJERCICIO 8.5

def describir_ciudad(nombre_ciudad, pais='españa'):
    print(f"\n{nombre_ciudad.title()} está en {pais.title()}")

describir_ciudad('paris', 'francia')
describir_ciudad('granada')
describir_ciudad('madrid')