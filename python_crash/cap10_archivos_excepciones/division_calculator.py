# EXCEPCIONES

# Manejar la excepción ZeroDivisionError

#print(5/0) # genera el error: ZeroDivisionError(objeto de excepcion)

# Usar bloques try-except y try-except-else

print("Give me two numbers, and I'll divide them.")
print("Enter 'q to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)