# DEJAR QUE EL USUARIO ELIJA CUANDO SALIR DEL PROGRAMA

prompt = "\nTell me something, and ill repeat it to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
    