# COPY A LIST

my_foods = ['pizza', 'falafel', 'carrot cake']
# Si fuese: friends_foods = my_foods siempre tendrian el mismo valor(las dos variables apuntan a la misma lista), 
# no se generaría una copia alternativa,por eso cogemos un trozo de la lista my_foods(my_foods[:]).
friends_foods = my_foods[:] 

my_foods.append('cogollos')
friends_foods.append('Ice cream')
print("Mi favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

