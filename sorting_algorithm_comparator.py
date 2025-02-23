"""
sorting_algorithm_comparator.py

CSC 506 - Design and Analysis of Algorithms
Colorado State University Global Campus

Author: Lincoln Quick
Date: February 9, 2025
Updated: February 23, 2025

Description:
    This script compares the performance of three sorting algorithms:
        - Bubble Sort (O(n²))
        - Merge Sort (O(n log n))
        - Quick Sort (O(n log n) average case, O(n²) worst case)
    
    The program generates different types of datasets (random, sorted, reverse sorted),
    runs each algorithm on various input sizes, measures execution time, and records
    the results for comparison.

    The results are displayed in the console and saved to an output file for analysis.

    The bubble sort, merge sort, and quick sort algorithms also have optimized versions
    that improve performance in certain scenarios. These optimized versions are also
    tested and compared against the standard implementations.

    Due to recurion depth limitations, the quick sort algorithm and the optimized quck sort 
    algorithms have iterative versions.

Usage:
    Run this script directly to execute sorting tests:
        $ python sorting_algorithm_comparator.py

Sections:
    1. Import Required Libraries
    2. Define Sorting Algorithms
    3. Define Optimized Alogrithms
    4. Define Data Generation Functions
    5. Define Sorting Test Functions
    6. Define Output Functions
    7. Main Execution Block

Output:
    - Prints execution time summaries to the console
    - Saves sorted results and performance metrics to a file
"""

# 1. Import Required Libraries
import random
import time

# 2. Define sorting algorithms
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

# 3. Optimized Sorting Algorithms
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

# 4. Define Data Generation Functions
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

# 5. Define Sorting Test Functions
def test_sorting_algorithms(sort_algorithms, data_generators, sizes, repetitions=3, output_file="sorting_results.txt"):
    """
    Tests sorting algorithms with different data generators and measures execution time.

    :param sort_algorithms: Dictionary of sorting functions {algorithm_name: function}.
    :param data_generators: Dictionary of data generation functions {data_type: function}.
    :param sizes: List of dataset sizes to test.
    :param repetitions: Number of times each test is repeated for accuracy.
    :param output_file: Filename to store the results.
    """
    
    results = []

    with open(output_file, "w") as file:
        file.write("Sorting Algorithm Performance Comparison\n")
        file.write("=" * 60 + "\n")

        for size in sizes:
            file.write(f"\nDataset Size: {size}\n")
            print(f"\nTesting Sorting Algorithms with {size} elements...\n")

            for data_type, data_generator in data_generators.items():
                dataset = data_generator(size)

                file.write(f"\nData Type: {data_type}\n")
                print(f"\nTesting on {data_type} dataset...\n")

                for algo_name, sort_function in sort_algorithms.items():
                    total_time = 0.0

                    for _ in range(repetitions):
                        test_data = dataset.copy()  # Ensure each run gets the same input
                        start_time = time.time()

                        # Handle cases where optimized versions require additional parameters
                        if "Quick Sort (Optimized)" in algo_name:
                            sort_function(test_data)
                        elif "Merge Sort (Optimized)" in algo_name:
                            sort_function(test_data, 0, len(test_data) - 1)
                        else:
                            sort_function(test_data)  # Standard sorts only take one argument

                        total_time += time.time() - start_time
                    
                    avg_time = total_time / repetitions
                    results.append((size, data_type, algo_name, avg_time))

                    file.write(f"{algo_name}: {avg_time:.6f} seconds\n")
                    print(f"{algo_name}: {avg_time:.6f} seconds")

    return results  # Return results for further analysis if needed

# 6. Define output functions
def display_results(results):
    """
    Displays sorting test results in a structured format.

    :param results: List of tuples (size, data_type, algo_name, avg_time).
    """
    print("\n" + "=" * 80)
    print(f"{'Dataset Size':<15}{'Data Type':<20}{'Algorithm':<30}{'Time (s)':<15}")
    print("=" * 80)

    for size, data_type, algo_name, avg_time in results:
        print(f"{size:<15}{data_type:<20}{algo_name:<30}{avg_time:.6f}")

    print("=" * 80)


def write_results_to_file(results, output_file="sorting_results_summary.txt"):
    """
    Writes sorting test results to a structured text file.

    :param results: List of tuples (size, data_type, algo_name, avg_time).
    :param output_file: Output file name.
    """
    with open(output_file, "w") as file:
        file.write("=" * 80 + "\n")
        file.write(f"{'Dataset Size':<15}{'Data Type':<20}{'Algorithm':<30}{'Time (s)':<15}\n")
        file.write("=" * 80 + "\n")

        for size, data_type, algo_name, avg_time in results:
            file.write(f"{size:<15}{data_type:<20}{algo_name:<30}{avg_time:.6f}\n")

        file.write("=" * 80 + "\n")

# 7. Main execution block
if __name__ == "__main__":
    # Define sorting algorithms (standard & optimized)
    sort_algorithms = {
        "Bubble Sort (Standard)": bubble_sort,
        "Bubble Sort (Optimized)": optimized_bubble_sort,
        "Merge Sort (Standard)": merge_sort,
        "Merge Sort (Optimized)": optimized_merge_sort,
        "Quick Sort (Standard)": iterative_quick_sort,
        "Quick Sort (Optimized)": iterative_optimized_quick_sort
    }

    # Define dataset generators 
    data_generators = {
        "Random Integers": generate_random_data,
        "Sorted Data": generate_sorted_data,
        "Reversed Data": generate_reverse_sorted_data,
        "Few Unique Elements": generate_duplicate_heavy_data
    }

    # Define dataset sizes to test
    dataset_sizes = [1_000, 5_000, 10_000, 20_000, 50_000]

    # Execute sorting tests
    results = test_sorting_algorithms(sort_algorithms, data_generators, dataset_sizes)

    # Display results
    display_results(results)

    # Save results to file
    write_results_to_file(results)

    print("\nSorting test execution completed. Results saved to 'sorting_results_summary.txt'.")
