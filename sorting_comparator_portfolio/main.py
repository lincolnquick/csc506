"""
main.py - Sorting Algorithm Comparator

CSC 506 - Design and Analysis of Algorithms
Colorado State University Global Campus

Author: Lincoln Quick
Date: February 9, 2025
Updated: February 28, 2025

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
    1. Define Sorting Algorithms
    2. Define Optimized Alogrithms
    3. Define Data Generation Functions
    4. Define Sorting Test Functions
    5. Define Output Functions
    6. Main Execution Block

Output:
    - Prints execution time summaries to the console
    - Saves sorted results and performance metrics to a file
"""

# 1. Define sorting algorithms
from sorting_algorithms import bubble_sort, merge_sort, iterative_quick_sort

# 2. Optimized Sorting Algorithms
from optimized_sorting_algorithms import optimized_bubble_sort, optimized_merge_sort, iterative_optimized_quick_sort

# 3. Define Data Generation Functions
from data_generation import generate_random_data, generate_sorted_data, generate_reverse_sorted_data, generate_duplicate_heavy_data

# 4. Define Sorting Test Functions
from sorting_tests import test_sorting_algorithms

# 5. Define output functions
from output_functions import display_results, write_results_to_file

# 6. Main execution block
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
