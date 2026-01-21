def int_to_str(i):
    """
    Convert a non-negative integer into its string representation without using built-in str().

    Parameters:
    i (int): A non-negative integer to be converted.

    Returns:
    str: The string representation of the given integer.

    Example:
    >>> int_to_str(123)
    '123'
    """
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ""

    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result

print(int_to_str(123),type(int_to_str(123))
