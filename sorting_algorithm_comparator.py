"""
sorting_algorithm_comparator.py

CSC 506 - Design and Analysis of Algorithms
Colorado State University Global Campus

Author: Lincoln Quick
Date: February 9, 2025

Description:
    This script compares the performance of three sorting algorithms:
        - Bubble Sort (O(n²))
        - Merge Sort (O(n log n))
        - Quick Sort (O(n log n) average case, O(n²) worst case)
    
    The program generates different types of datasets (random, sorted, reverse sorted),
    runs each algorithm on various input sizes, measures execution time, and records
    the results for comparison.

    The results are displayed in the console and saved to an output file for analysis.

Usage:
    Run this script directly to execute sorting tests:
        $ python sorting_algorithm_comparator.py

Sections:
    1. Import Required Libraries
    2. Define Sorting Algorithms
    3. Define Data Generation Functions
    4. Define Sorting Test Functions
    5. Define Output Functions
    6. Main Execution Block

Output:
    - Prints execution time summaries to the console
    - Saves sorted results and performance metrics to a file
"""

# Import Required Libraries
import random
import time

# Define sorting algorithms
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


def quick_sort(arr):
    """
    Implements Quick Sort algorithm iteratively to prevent recursion depth issues.

    Time Complexity:
        - Best Case: O(n log n)
        - Average Case: O(n log n)
        - Worst Case: O(n²) (if poorly chosen pivot)

    Space Complexity: O(log n) (stack usage in recursion)

    :param arr: List of numbers to be sorted.
    :return: Sorted list (new list, original remains unchanged).
    """
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]  # Stack to store subarrays that need sorting

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue  # Skip if only one element or invalid range

        pivot_index = partition(arr, left, right)

        # Push smaller partition first (helps balance recursion depth)
        if pivot_index - left < right - pivot_index:
            stack.append((pivot_index + 1, right))
            stack.append((left, pivot_index - 1))
        else:
            stack.append((left, pivot_index - 1))
            stack.append((pivot_index + 1, right))

    return arr


def partition(arr, left, right):
    """
    Lomuto Partition Scheme: Chooses last element as pivot, partitions list.

    :param arr: List to partition.
    :param left: Left boundary.
    :param right: Right boundary.
    :return: Final pivot index.
    """
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[right] = arr[right], arr[i + 1]  # Swap pivot to correct position
    return i + 1
         

# Define data generation functions
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


def generate_nearly_sorted_data(size, swaps=5):
    """
    Generates a nearly sorted list where a few elements are randomly swapped.
    
    :param size: Number of elements in the list.
    :param swaps: Number of random swaps to introduce disorder.
    :return: Nearly sorted list of integers.
    """
    arr = list(range(size))
    for _ in range(swaps):
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]  # Swap two elements
    return arr


def generate_duplicate_heavy_data(size, unique_values=10):
    """
    Generates a list with a limited set of unique values, increasing the likelihood of duplicates.
    
    :param size: Number of elements in the list.
    :param unique_values: Number of unique values allowed.
    :return: List of integers with heavy duplication.
    """
    return [random.randint(0, unique_values - 1) for _ in range(size)]

# Define sorting test functions
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
        file.write("="*50 + "\n")

        for size in sizes:
            file.write(f"\nDataset Size: {size}\n")
            print(f"\nTesting Sorting Algorithms with {size} elements...\n")

            for data_type, data_generator in data_generators.items():
                dataset = data_generator(size)

                file.write(f"\nData Type: {data_type}\n")
                print(f"Testing on {data_type} dataset...\n")

                for algo_name, sort_function in sort_algorithms.items():
                    total_time = 0.0

                    for _ in range(repetitions):
                        test_data = dataset.copy()  # Ensure each run gets the same input
                        start_time = time.time()
                        sort_function(test_data)
                        total_time += time.time() - start_time
                    
                    avg_time = total_time / repetitions
                    results.append((size, data_type, algo_name, avg_time))

                    file.write(f"{algo_name}: {avg_time:.6f} seconds\n")
                    print(f"{algo_name}: {avg_time:.6f} seconds")

    return results  # Return results for further analysis if needed

# Define output functions
def display_results(results):
    """
    Displays sorting test results in a structured format.

    :param results: List of tuples (size, data_type, algo_name, avg_time).
    """
    print("\n" + "="*60)
    print(f"{'Dataset Size':<15}{'Data Type':<20}{'Algorithm':<20}{'Time (s)':<10}")
    print("="*60)

    for size, data_type, algo_name, avg_time in results:
        print(f"{size:<15}{data_type:<20}{algo_name:<20}{avg_time:.6f}")

    print("="*60)


def write_results_to_file(results, output_file="sorting_results_summary.txt"):
    """
    Writes sorting test results to a structured text file.

    :param results: List of tuples (size, data_type, algo_name, avg_time).
    :param output_file: Output file name.
    """
    with open(output_file, "w") as file:
        file.write("="*60 + "\n")
        file.write(f"{'Dataset Size':<15}{'Data Type':<20}{'Algorithm':<20}{'Time (s)':<10}\n")
        file.write("="*60 + "\n")

        for size, data_type, algo_name, avg_time in results:
            file.write(f"{size:<15}{data_type:<20}{algo_name:<20}{avg_time:.6f}\n")

        file.write("="*60 + "\n")

# Main execution block
if __name__ == "__main__":
    # Define sorting algorithms
    sort_algorithms = {
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    # Define dataset generators
    data_generators = {
        "Random Integers": generate_random_data,
        "Sorted Data": generate_sorted_data,
        "Reversed Data": generate_reverse_sorted_data,
        "Few Unique Elements": generate_duplicate_heavy_data
    }

    # Define dataset sizes to test
    dataset_sizes = [100, 1_000, 5_000, 10_000, 20_000, 50_000]

    # Execute sorting tests
    results = test_sorting_algorithms(sort_algorithms, data_generators, dataset_sizes)

    # Display results
    display_results(results)

    # Save results to file
    write_results_to_file(results)

    print("\nSorting test execution completed. Results saved to 'sorting_results_summary.txt'.")