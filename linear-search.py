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

# Sample product list (unsorted)
products = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# Product to search for
target_product = 'grape'

# Perfrom a linear search
result = linear_search(products, target_product)

# Print the results
if result != -1:
    print(f"Product '{target_product}' was found at index {result}.")
else:
    print(f"Product '{target_product}' was not found in the catalog.")