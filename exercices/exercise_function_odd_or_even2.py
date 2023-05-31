nb_user = int(input("Type a number (an integer) "))

def even_or_odd(number:int) -> bool:
    """Takes an integer, return true or false

    Args:
        number (int): number is tested

    Returns:
        bool: True if even, false if odd
    """
    if number %2 == 0:
        print(True)
    else:
        print(False)

even_or_odd(nb_user)