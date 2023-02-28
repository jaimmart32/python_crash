# 11.1 y 11.2

def get_city(city, country, population=0):
    """Devuelve una cadena sencilla con la ciudad y el pais."""
    if population:
        city_str = f"{city.title()}, {country.title()} - habitantes {population}"
        return city_str
    else:
        city_str = f"{city.title()}, {country.title()}"
        return city_str