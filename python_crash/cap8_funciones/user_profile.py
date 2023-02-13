# USAR ARGUMENTOS DE PALABRA CLAVE ARBITRARIOS

# ** hace que python cree un diccionario llamado user_info en vez de una tupla
def build_profile(first, last, **user_info):
    """Crea un diccionario con todo lo que sabemos sobre un usuario."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)