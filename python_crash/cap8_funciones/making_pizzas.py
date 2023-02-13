# IMPORTAR UN MODULO COMPLETO

import pizza

pizza.make_pizza('peperoni')
pizza.make_pizza('mushrooms', 'green peppers', 'extra cheese')

# IMPORTAR FUNCIONES ESPECIFICAS

from pizza1 import make_pizzas

make_pizzas(15, 'prosciutto')
make_pizzas(10, 'mushrooms', 'green peppers')

# USAR as PARA DAR UN ALIAS A UNA FUNCION

from pizza import make_pizza as mp

mp('pepperoni', 'green peppers')

# USAR as PARA DAR UN ALIAS A UN MODULO

import pizza as p

p.make_pizza(16, 'pepper')

# IMPORTAR TODAS LAS FUNCIONES DE UN MODULO

from pizza import *# Cuidado con los modulos grandes, 
                   # puede haber una funcion que se llame igual causando conflicto sobreescribiendolas

make_pizzas(15, 'pepp')
make_pizzas(10, 'mushrooms', 'red peppers')