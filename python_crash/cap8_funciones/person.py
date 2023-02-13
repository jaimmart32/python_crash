# DEVOLVER UN DICCIONARIO

def build_person(first_name, last_name, age=None):
    """Devuelve un diccionario de información sobre una persona."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)