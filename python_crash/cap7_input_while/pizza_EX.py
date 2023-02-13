prompt = "\nIntroduce un ingrediente para la pizza: "
prompt += "\n(Introduzca 'quit' para terminar)"

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f"\nSe añadira {message} a su pizza.")
        