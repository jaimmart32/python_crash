# ASOCIAR EVENTOS QUE TERMINEN EL PROGRAMA A FLAGS(active)

prompt = "\nTell me something, and ill repeat it to you: "
prompt += "\nEnter 'quit' to end the program.   "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
