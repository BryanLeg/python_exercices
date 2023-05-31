nb_user1 = float(input('type a number '))
nb_user2 = float(input('type a second number '))
nb_user3 = float(input('type a third number '))

def average(nb1, nb2, nb3):
    """Takes 3 numbers, return the average

    Args:
        nb1 (float): a positive float 
        nb2 (float): a positive float 
        nb3 (float): a positive float 

    returns:
        nb (float): the average
    """
    print((nb1 + nb2 + nb3)/3)

average(nb_user1, nb_user2, nb_user3)