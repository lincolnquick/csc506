"""
sorting_algorithms.py - Sorting Algorithm Comparator

CSC 506 - Design and Analysis of Algorithms
Colorado State University Global Campus

Author: Lincoln Quick
Date: February 9, 2025
Updated: March 9, 2025

Description:
    This module contains implementations of three sorting algorithms:
        - Bubble Sort
        - Merge Sort
        - Quick Sort
    
"""
import random

def bubble_sort(arr):
    """
    Implements the Bubble Sort algorithm.
    
    Time Complexity:
        - Best Case: O(n) (already sorted)
        - Average Case: O(n²)
        - Worst Case: O(n²)
    
    Space Complexity: O(1) (in-place sorting)
    
    :param arr: List of numbers to be sorted.
    :return: None (modifies input list in-place).
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                swapped = True
        if not swapped:  # Optimization: Stop if no swaps occurred in a pass
            break


def merge_sort(arr):
    """
    Implements the Merge Sort algorithm.
    
    Time Complexity:
        - Best Case: O(n log n)
        - Average Case: O(n log n)
        - Worst Case: O(n log n)
    
    Space Complexity: O(n) (extra space for merging)
    
    :param arr: List of numbers to be sorted.
    :return: Sorted list (new list, original remains unchanged).
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return _merge(left_half, right_half)


def _merge(left, right):
    """
    Merges two sorted lists into one sorted list.

    :param left: Left sorted sublist.
    :param right: Right sorted sublist.
    :return: Merged sorted list.
    """
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr, low=0, high=None):
    """
    Implements Quick Sort algorithm using Lomuto Partition Scheme.
    Uses iterative tail call optimization to reduce recursion depth.

    :param arr: List of numbers to be sorted.
    :param low: Left boundary of the sorting range.
    :param high: Right boundary of the sorting range.
    :return: None (modifies input list in-place).
    """
    if high is None:
        high = len(arr) - 1

    while low < high:
        pivot_index = randomized_partition(arr, low, high)

        # Optimize recursion depth by processing the smaller partition first
        if pivot_index - low < high - pivot_index:
            quick_sort(arr, low, pivot_index - 1)
            low = pivot_index + 1  # Tail call elimination
        else:
            quick_sort(arr, pivot_index + 1, high)
            high = pivot_index - 1

def iterative_quick_sort(arr):
    """
    Iterative implementation of Quick Sort using a manual stack.
    
    :param arr: List of numbers to be sorted.
    :return: None (modifies input list in-place).
    """
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = randomized_partition(arr, low, high)

            # Push larger partition last (process smaller one first for efficiency)
            if pivot_index - low < high - pivot_index:
                stack.append((pivot_index + 1, high))
                stack.append((low, pivot_index - 1))
            else:
                stack.append((low, pivot_index - 1))
                stack.append((pivot_index + 1, high))

def randomized_partition(arr, low, high):
    """
    Selects a random pivot and partitions the array using Lomuto’s scheme.
    Improves Quick Sort performance on nearly sorted data.

    :param arr: List to partition.
    :param low: Left boundary.
    :param high: Right boundary.
    :return: Final pivot index.
    """
    pivot_index = random.randint(low, high)  # Select a random pivot
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot to end
    return partition(arr, low, high)

def partition(arr, low, high):
    """
    Lomuto Partition Scheme:
    Moves elements smaller than pivot to the left, and larger to the right.
    
    :param arr: List to partition.
    :param low: Left boundary.
    :param high: Right boundary.
    :return: Final pivot index.
    """
    pivot = arr[high]  # Last element as pivot
    i = low - 1  # Smaller element index

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap smaller elements to left

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot into place
    return i + 1  # Return final pivot position