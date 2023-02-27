# 10.11

import json

favourite_number = input("What is your favourite number? ")

filename = 'favourite_numbers.json'
with open(filename, 'w') as f:
    json.dump(favourite_number, f)