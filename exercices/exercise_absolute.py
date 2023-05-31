def product_of_absoluts_values(number1:int, number2:int) -> int:
    """Takes 2 numbers, return the product of absolutes values

    Args:
        number1 (int): first number is tested
        number2 (int): second number is tested

    Returns:
        int: _description_
    """
    if number1 < 0:
        number1 = - number1
    if number2 < 0:
        number2 = - number2
    return number1 * number2

print(product_of_absoluts_values(-6,8))