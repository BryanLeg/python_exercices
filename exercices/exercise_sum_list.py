nb_user1 = int(input('type a number '))
nb_user2 = int(input('type a second number '))
nb_user3 = int(input('type a third number '))
nb_user4 = int(input('type a fourth number '))

nb_list = [nb_user1, nb_user2, nb_user3, nb_user4]

def sum_list(list: list) -> float:
    """Takes a list, return sum

    Args:
        list (list): list of numbers

    Returns:
        float: sum of numbers in the list
    """
    result = 0
    for nb in list:
        result += nb
    return result

print(sum_list(nb_list))