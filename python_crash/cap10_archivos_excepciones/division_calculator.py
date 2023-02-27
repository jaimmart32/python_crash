# EXCEPCIONES

# Manejar la excepción ZeroDivisionError

#print(5/0) # genera el error: ZeroDivisionError(objeto de excepcion)

# Usar bloques try-except

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
