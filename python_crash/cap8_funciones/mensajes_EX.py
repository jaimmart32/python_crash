# EJERCICIO 8.1

def mostrar_mensaje():
    print("Estoy aprendiendo sobre funciones, argumentos y parámetros en python.")

mostrar_mensaje()

# EJERCICIO 8.2

def libro_favorito(título):
    print(f"\nUno de mis libros favoritos es {título}")

libro_favorito('tao te king')

print("****************************************************************************")
# EJERCICIO 8.9

def mostrar_mensajes(msgs):
    for msg in msgs:
        print(msg)
mensajes = ['yeah!', 'ok', 'ni de coña', 'lol']

mostrar_mensajes(mensajes)

# EJERCICIO 8.10 y 8.11

mensajes_enviados = []
def enviar_mensajes(msgs):
    """Muestra y envia los mensajes a la lista de mensajes enviados."""
    while msgs:
        msg = msgs.pop()
        print(msg)

        mensajes_enviados.append(msg)

enviar_mensajes(mensajes)
print(mensajes)
print(mensajes_enviados)