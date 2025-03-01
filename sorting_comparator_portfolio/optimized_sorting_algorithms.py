from sorting_algorithms import partition

def optimized_bubble_sort(arr):
    """ Optimized with adaptive pass count """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        last_swap = 0
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                last_swap = j
        if not swapped:
            break # Stop if no swaps occurred
        n = last_swap + 1  # Reduce pass count to last swap index + 1

def optimized_merge_sort(arr, left=0, right=None):
    """ Optimized with Hybrid Insertion Sort """
    if right is None:
        right = len(arr) - 1
    if right - left <= 10:
        insertion_sort(arr, left, right)
        return
    if left < right:
        mid = (left + right) // 2
        optimized_merge_sort(arr, left, mid)
        optimized_merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    """Optimized Merge Helper Function (works in-place)"""
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    arr[k:right + 1] = left_part[i:] + right_part[j:]  

def optimized_quick_sort(arr, low, high):
    """ Optimized Quick Sort with Median-of-Three Pivot and Hybrid Insertion Sort. """
    if low >= high:
        return  # Base case: Stop recursion if low >= high
    
    if high - low <= 10:  # Use Insertion Sort for small partitions
        insertion_sort(arr, low, high)
        return

    pivot_index = median_of_three_partition(arr, low, high)  # Improved pivot selection
    optimized_quick_sort(arr, low, pivot_index - 1)  # Sort left subarray
    optimized_quick_sort(arr, pivot_index + 1, high)  # Sort right subarray

def iterative_optimized_quick_sort(arr):
    """Iterative Quick Sort using Median-of-Three for better pivot selection."""
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            if high - low <= 10:
                insertion_sort(arr, low, high)
                continue
            
            pivot_index = median_of_three_partition(arr, low, high)

            # Push larger partition last (process smaller one first)
            if pivot_index - low < high - pivot_index:
                stack.append((pivot_index + 1, high))
                stack.append((low, pivot_index - 1))
            else:
                stack.append((low, pivot_index - 1))
                stack.append((pivot_index + 1, high))

def median_of_three_partition(arr, low, high):
    """
    Selects the median of three elements (first, middle, last) as pivot.
    Uses Lomuto Partition Scheme.

    :param arr: List to partition.
    :param low: Left boundary.
    :param high: Right boundary.
    :return: Final pivot index.
    """
    mid = (low + high) // 2
    pivot_candidates = [arr[low], arr[mid], arr[high]]
    pivot_candidates.sort()
    pivot = pivot_candidates[1]  # Median value as pivot

    pivot_index = arr.index(pivot)  # Find actual index
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot to end
    return partition(arr, low, high)  # Use Lomuto partitioning


def insertion_sort(arr, left, right):
    """ Insertion Sort used in hybrid Quick Sort for small subarrays. """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key