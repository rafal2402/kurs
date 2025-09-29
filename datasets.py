result = []
for x in range(11):
    result.append(x ** 3)

print(f'List: {result}')

result = [x ** 3 for x in range(11)]
print(f'List: {result}')

result = [x ** 3 for x in range(11) if x % 2 == 0]
print(f'List: {result}')

import math
result = [int(math.pow(x, 3)) for x in range(11) if x % 2 == 0]
print(f'List: {result}')

brands = ["Volvo", "Mercedes", "Toyota"]
colors = ["Black", "White", "Pink", "Red", "Blue"]
combinations = [(brand, color) for brand in brands for color in colors]
print(combinations)

positions = [1, 2, 3, 4, 5, 6]
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
combinations = [(position, digit) for position in positions for digit in digits]
print(combinations)
print(len(combinations))


