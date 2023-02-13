# SORT A LIST WITH sort()

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

print("**************************************************************************************************************************\n")
# SORT IN REVERSE ORDER

cars.sort(reverse=True)
print(cars)

print("**************************************************************************************************************************\n")
#SORT TEMPORARELY A LIST WITH sorted()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nAqui esta la lista original:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nAqui esta la original de nuevo, solo era temporal con sorted.")
print(cars)

print("**************************************************************************************************************************\n")
# PRINT A LIST IN REVERSE ORDER

cars.reverse()
print("La lista invertida:")
print(cars)

print("**************************************************************************************************************************\n")
# DISCOVER LENGTH OF LIST

length = len(cars)
print(f"This list has {length} elements.")