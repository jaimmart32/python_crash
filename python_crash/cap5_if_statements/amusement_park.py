age = 12

if age < 4:
    print("Your admision cost is $0.")
elif age < 18:
    print("Your admision cost is $25.")
else:
    print("Your admision cost is $40.")

#IF ELIF
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admision cost is ${price}.")

#MULTIPLES BLOQUES ELIF
age = 67

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admision cost is ${price}.")

#OMITIR EL BLOQUE ELSE
age = 67

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admision cost is ${price}.")
