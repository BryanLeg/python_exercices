base_list = ["one", 2, 3.4, "five, six"]

def reverse(list: list) -> list:
    """Takes a list, return its inverse

    Args:
        list (list): the list to revert

    Returns:
        list: reverted list
    """
    # new_list = list.copy()
    # new_list.reverse()
    # print(new_list)
    list2 = list.copy()
    for i in range(0, len(list2)//2):
        list2[i], list2[-1 - i] = list2[-1 - i], list2[i]
    return list2

reverse(base_list)