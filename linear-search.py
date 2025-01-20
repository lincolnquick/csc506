def linear_search(products, target):
    """
    Perform a linear search to find a product in the list.

    :param products: List of products names.
    :param target: The product name to search for.
    :return: Index position if found, otherwise -1.
    """
    for index in range(len(products)):
        if products[index] == target:
            return index
    return -1

