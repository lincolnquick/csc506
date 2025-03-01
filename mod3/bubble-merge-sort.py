# Lincoln Quick
# 2025-02-02
# CSC 506 - Module 3 Critical Thinking Assignment: Bubble Sort, Merge Sort.
# "Dive into the task of enhancing the efficiency of a hospital's patient records system by comparing the 
# Bubble Sort and Merge Sort algorithms.

# Algorithm: Bubble Sort and Merge Sort
# Analysis (one page, excluding cover and references): Analyze the time complexity of both sorting algorithms, 
# elucidate the conditions under which each performs optimally in the medical records context, and discuss the 
# critical problem of sorting in healthcare. Justify the chosen data structures and consider external factors 
# affecting efficiency and the lower bound.
# Please ensure that your submission includes the following components:

# Source code file(s) containing the program implementation.
# A 1-page paper (excluding the cover and references) explaining the program's purpose, the obstacles faced during 
# its development, and the skills acquired. The paper should also include screenshots showcasing the successful 
# execution of the program.

# Please make sure to follow the APA guidelines for formatting and referencing in the paper, including the cover 
# page, introduction, content, conclusion, and references sections.

# Data Structure for Patient Records
import random
import datetime
import time

# Sample first and last names
first_names = ["Jessica", "Jamal", "Theresa", "Matthew", "Donald", "Robert", "Jose", "Camilla", "Grace", "Hannah"]
last_names = ["Jefferson", "Ericson", "Vanderbilt", "Williams", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson"]

# Function to generate random patient records
def generate_patient_records(num_records=10):
    patient_records = []
    for _ in range(num_records):
        patient = {
            "ID": random.randint(1000, 9999),  # Generate a 4-digit random ID
            "Name": f"{random.choice(last_names)}, {random.choice(first_names)}",
            "Age": random.randint(18, 80),  # Age between 18 and 80
            "Admission Date": (datetime.datetime.today() - datetime.timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
        }
        patient_records.append(patient)
    return patient_records

# Generate 10 random patient records
patients = generate_patient_records(10)

# Bubble Sort
def bubble_sort(records, key):
    """
    Sort a list of patient records using the Bubble Sort algorithm.

    :param records: List of patient records.
    :param key: The key to sort the records by.
    :return: Sorted list of patient records.
    """
    n = len(records)
    for i in range (n - 1):
        swapped = False
        for j in range(n - i - 1):
            if records[j][key] > records[j + 1][key]:
                records[j], records[j+1] = records[j + 1], records[j]
                swapped = True
        if not swapped:
            break

# Merge Sort
def merge_sort(records, key):
    """
    Sort a list of patient records using the Merge Sort algorithm.

    :param records: List of patient records.
    :param key: The key to sort the records by.
    :return: Sorted list of patient records.
    """
    if len(records) > 1:
        mid = len(records) // 2
        left_half = records[:mid]
        right_half = records[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:
                records[k] = left_half[i]
                i += 1
            else:
                records[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            records[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            records[k] = right_half[j]
            j += 1
            k += 1

# Generate random patient records, print original records, sort by name, print results, and seconds to sort.
def test_sorting_algorithms(times, sort_key, output_file):

    patients = generate_patient_records(times)

    print("\nOriginal Patient Records:")
    for patient in patients:
        print(patient)

    # Bubble Sort Test
    bubble_sorted_patients = patients.copy()
    start_time = time.time()
    bubble_sort(bubble_sorted_patients, sort_key)
    bubble_sort_time = time.time() - start_time

    # Merge Sort Test
    merge_sorted_patients = patients.copy()
    start_time = time.time()
    merge_sort(merge_sorted_patients, sort_key)
    merge_sort_time = time.time() - start_time

    # Write results to file
    with open(output_file, "a") as file:
        file.write(f"\n\nSorting {times} Patient Records by {sort_key}:\n")
 
        file.write(f"\nBubble Sort Time: {bubble_sort_time:.6f} seconds\n")
        file.write(f"\nMerge Sort Time: {merge_sort_time:.6f} seconds\n")

        file.write("\nBubble Sorted Records (for accuracy check):\n")
        file.write("\n".join(str(record) for record in bubble_sorted_patients))
        file.write("\Merge Sorted Records (for accuracy check):\n")
        file.write("\n".join(str(record) for record in merge_sorted_patients))
        file.write("\n" + "="*80 + "\n")
    
    # Print performance comparison to screen
    print(f"\nSorting {times} patient records by {sort_key}:")
    print(f"Bubble Sort Execution Time: {bubble_sort_time:.6f} seconds")
    print(f"Merge Sort Execution Time: {merge_sort_time:.6f} seconds")
        

# Test the sorting algorithms with 10, 100, 1000, and 10000 patient records sorted by name
output_filename = "sorting_results.txt"
with open(output_filename, "w") as file:
    file.write("Sorting Algorithm Performance Comparison\n")
    file.write("="*80 + "\n")

# Run sorting tests with different dataset sizes
for size in [10, 100 , 1000, 10000]:
    test_sorting_algorithms(size, "Name", output_filename)

