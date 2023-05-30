nb_user = int(input("Type a number (an integer) "))

def even_or_odd(number):
    '''Takes an integer, return even or odd'''
    if number %2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")

even_or_odd(nb_user)