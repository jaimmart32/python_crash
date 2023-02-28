#def get_formatted_name(first, last):
#    """Genera un nombre completo con formato adecuado."""
#    full_name = f"{first} {last}"
#    return full_name.title()


# Una prueba que falla

def get_formatted_name(first, last, middle=''):
    """Genera un nombre completo con formato adecuado."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

# Responder a una prueba fallida