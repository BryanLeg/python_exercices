import random

list = [random.randrange(100) for x in range(1000)]

print(list)

new_list = [x for x in list if x < 10]

print(new_list)