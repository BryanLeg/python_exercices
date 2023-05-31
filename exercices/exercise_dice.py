import random

list = [random.randrange(101) for _ in range(1000)]

print(list)

list_lower_10 = [elt for elt in list if elt < 10]

print(list_lower_10)