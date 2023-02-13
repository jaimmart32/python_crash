ciudades = {
    'madrid': {
        'país': 'españa',
        'población': 6825005,
        'curiosidad': 'es la capital del país',
        },

    'dubai': {
        'país': 'dubai',
        'población': 3300000,
        'curiosidad': 'es una ciudad protegida de la degeneración de occidente', 
        },

    'venecia': {
       'país': 'italia',
        'población': 270884,
        'curiosidad': 'tiene calles sumergidas en agua', 
        },
}

for ciudad, info_ciudad in ciudades.items():
    print(f"\n{ciudad.title()} esta en {info_ciudad['país'].title()},tiene {info_ciudad['población']}.")
    print(f"La curiosidad de {ciudad.title()}, {info_ciudad['curiosidad']}.")
    
    