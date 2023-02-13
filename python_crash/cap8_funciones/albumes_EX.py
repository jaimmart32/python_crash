# EJERCICIO 8.7 y 8.8

def hacer_album(artista, titulo, numero_canciones=None):
    """Devuelve un diccionario de información sobre una persona."""
    album = {'artista': artista.title(), 'titulo': titulo}
    if numero_canciones:
        album['num_canciones'] = numero_canciones
    return album

while True:
    print("\nWich album do you want to register?")
    print("(enter 'q' at any time to quit)")

    artista = input("Artist name: ")
    if artista == 'q':
        break

    titulo = input("ALbum's title: ")
    if titulo == 'q':
        break

    numero_canciones = input("Do you know how many songs does it have? (if you dont know press enter)")
    if numero_canciones:
        num_songs = int(numero_canciones)
        album = hacer_album(artista, titulo,numero_canciones=num_songs)
        print(album)
    else:   
        album = hacer_album(artista, titulo)
        print(album)
"""album_0 = hacer_album('2pac', 'All eyes on me', numero_canciones=21)
print(album_0)

album_1 = hacer_album('biggie', 'juicy')
print(album_1)

album_2 = hacer_album('system of a down', 'steal this album')
print(album_2)"""