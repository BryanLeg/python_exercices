def even_or_odd():
    '''Takes an integer, return even or odd'''
    nb_user = int(input("Type a number (an integer) "))
    if nb_user %2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")

even_or_odd()