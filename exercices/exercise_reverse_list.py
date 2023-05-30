base_list = ["one", 2, 3.4, "five, six"]

def reverse(list):
    '''Takes a list, return its inverse'''
    new_list = list.copy()
    new_list.reverse()
    print(new_list)

reverse(base_list)