# VALORES DE RETORNO(return)

def get_formatted_name(first_name, last_name):
    """Devuelve un nombre completo, con un formato adecuado."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Hacer un argumento opcional

def get_formatted_name_op(first_name, last_name, middle_name=''):
    """Devuelve un nombre completo, con un formato adecuado."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
       full_name = f"{first_name} {last_name}" 
    return full_name.title()

musician = get_formatted_name_op('jimi', 'hendrix')
print(musician)

musician = get_formatted_name_op('jaime', 'martinez', 'joaquín')
print(musician)