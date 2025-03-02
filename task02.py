import random

def find_exclusive_numbers(min:int, max:int, quantity:int) -> list:
    """
    Generates a sorted list of unique random numbers within the given range.

    Args:
        min (int): The minimum value of the range.
        max (int): The maximum value of the range.
        quantity (int): The number of unique random numbers to generate.

    Returns:
        list: A sorted list of unique random numbers.
    """
    unique_numbers = random.sample(range(min, max + 1), quantity)
    return sorted(unique_numbers)

def get_numbers_ticket(min:int, max:int, quantity:int) -> list:
    """
    Validates the input parameters and returns a sorted list of unique random numbers if valid.

    Args:
        min (int): The minimum value of the range.
        max (int): The maximum value of the range.
        quantity (int): The number of unique random numbers to generate.

    Returns:
        list: A sorted list of unique random numbers if valid, otherwise an empty list.
    """
    if not all(isinstance(arg, int) for arg in [min, max, quantity]):
        return []
    if min >= 1 and max < 1000 and quantity > 0:
        if quantity > (max - min + 1):
            return []
        return find_exclusive_numbers(min, max, quantity)
    else:
        return []


# Test the function

print(get_numbers_ticket(1, 36, 5)) # example [4, 15, 23, 28, 37]
print(get_numbers_ticket(1, 49, 60)) # []
print(get_numbers_ticket(1, 546, 6)) #[] example [4, 15, 23, 28, 37, 45]
print(get_numbers_ticket(1, 4, 10)) #[]
print(get_numbers_ticket(1, 49, 0)) #[]
print(get_numbers_ticket(1, 49, -6)) #[]
print(get_numbers_ticket(1, '3', 49)) #[]
print(get_numbers_ticket(1, 49, 'abc')) #[]


