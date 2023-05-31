for i in range(101):
    print(i, end=' : ')
    # if i%3 and i%5:
    #     print('Fizz-Fuzz')
    if i%3 == 0:
        print("Fizz", end=' ')
    elif i%5 == 0:
        print("Fuzz", end=' ')
    # else:
    #     print(i)
    print()