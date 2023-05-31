nb_user = int(input("Type a number (an integer) "))

def even_or_odd(number:int):
    """Takes an integer, return even or odd

    Args:
        number (int): number is tested
    """
    if number %2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")

even_or_odd(nb_user)