numero = input("Dime un número y te dire si es multiplo de diez: ")
numero = int(numero)

if numero % 10 == 0:
    print(f"\nEn efecto, {numero} es multiplo de diez.")
else:
    print(f"{numero} no es multiplo de diez.")
