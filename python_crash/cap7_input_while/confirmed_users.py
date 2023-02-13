# while CON LISTAS Y DICCIONARIOS

# Empieza con usuarios que hay ue verificar, y una lista vacía
#  para alojar a los usuarios confirmados.
unconfirmed_users = ['alice', 'bryan', 'tupac']
confirmed_users = []

# Verifica cada usuario hasta que ya no hay usuarios sin confirmar.
# Mueve a cada usuario verificado a la lista de usuarios confirmados.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())  