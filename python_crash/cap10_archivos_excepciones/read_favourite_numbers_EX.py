# 10.11

import json

filename = 'favourite_numbers.json'
with open(filename) as f:
    favourite_number = json.load(f)

print(f"Your favourite number is {favourite_number}")