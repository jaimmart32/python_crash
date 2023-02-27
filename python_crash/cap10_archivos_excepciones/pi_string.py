# TRABAJAR CON EL CONTENIDO DE UN ARCHIVO

filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# ARCHIVOS GRANDES

filename2 = 'text_files/pi_million_digits.txt'

with open(filename2) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthdate = input("Enter your birthday, in form mmddyy: ")
if birthdate in pi_string:
    print("Your birthday is in the first 200 numbers!")
else:
    print("It is not in th first 200 digits!")