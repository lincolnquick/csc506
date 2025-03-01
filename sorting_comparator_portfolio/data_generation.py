import random

def generate_random_data(size, lower_bound=0, upper_bound=10000):
    """
    Generates a list of random integers within the specified range.
    
    :param size: Number of elements in the list.
    :param lower_bound: Minimum integer value.
    :param upper_bound: Maximum integer value.
    :return: List of random integers.
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]


def generate_sorted_data(size):
    """
    Generates a sorted list of integers in ascending order.
    
    :param size: Number of elements in the list.
    :return: Sorted list of integers.
    """
    return list(range(size))


def generate_reverse_sorted_data(size):
    """
    Generates a list sorted in descending order.
    
    :param size: Number of elements in the list.
    :return: Reverse sorted list of integers.
    """
    return list(range(size, 0, -1))


def generate_duplicate_heavy_data(size, unique_values=10):
    """
    Generates a list with a limited set of unique values, increasing the likelihood of duplicates.
    
    :param size: Number of elements in the list.
    :param unique_values: Number of unique values allowed.
    :return: List of integers with heavy duplication.
    """
    return [random.randint(0, unique_values - 1) for _ in range(size)]