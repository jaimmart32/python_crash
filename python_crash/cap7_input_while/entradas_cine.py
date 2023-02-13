prompt = "\nHow old are you? "
prompt += "\n(enter 'quit' to exit)"

age = ""
while True:
    age = input(prompt)
    if age == 'quit':
        break
    if age:
        age = int(age)
    else:
        break

    if age < 3:
        print(f"\nIt is free since you are {age} years old.")
    elif age <= 12:
        print(f"\nIt will be $8 since you are {age} years old.")
    else:
        print(f"\nIt will be $12 since you are older than 12 years old.")
