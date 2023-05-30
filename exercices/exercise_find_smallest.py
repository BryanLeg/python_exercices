nb_user1 = int(input("type a number "))
nb_user2 = int(input("type a second number "))
nb_user3 = int(input("type a third number "))

def smallest_number(number1, number2, number3):
    '''Takes 3 numbers, return the smallest'''
    if number1 < number2 and number1 < number3:
        print(f'{number1} is the smallest number')
    elif number2 < number3 and number2 < number1:
        print(f'{number2} is the smallest number')
    else:
        print(f'{number3} is the smallest number')

smallest_number(nb_user1, nb_user2, nb_user3)