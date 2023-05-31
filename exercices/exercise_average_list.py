nb_user1 = int(input('type a number '))
nb_user2 = int(input('type a second number '))
nb_user3 = int(input('type a third number '))
nb_user4 = int(input('type a fourth number '))

nb_list = [nb_user1, nb_user2, nb_user3, nb_user4]

def average_list(list: list) -> float:
    """takes a list of numbers, return the average

    Args:
        list (list): a list of numbers

    Returns:
        float: the average of list's numbers
    """
    return sum(list)/len(list)

print(average_list(nb_list))