squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

# MIN, MAX AND SUM OF A LIST OF NUMBERS

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))

print(max(digits))

print(sum(digits))

# CREATE A LIST OF NUMBERS WITH A COMPRESION LIST

squares = [value**2 for value in range(1,11)] #<<<<<<<-------------comprimida wacho, y sin : en el for!
print(squares)

