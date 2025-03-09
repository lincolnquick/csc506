"""
output_functions.py - Sorting Algorithm Comparator

CSC 506 - Design and Analysis of Algorithms
Colorado State University Global Campus

Author: Lincoln Quick
Date: February 9, 2025
Updated: March 9, 2025

Description:
    This module contains functions to display and write sorting test results.

"""
import csv

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
        
    print(f"\nResults have been successfully saved to '{output_file}' for review.\n")

def write_results_to_csv(results, csv_file="sorting_results_summary.csv"):
    """
    Writes sorting test results to a CSV file for easier data analysis.
    
    :param results: List of typles (size, data_type, algo_name, avg_time).
    :param csv_file: Output CSV file name.
    """

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow((["Dataset Size", "Data Type", "Algorithm", "Time (s)"]))

        # Write each result row
        for size, data_type, algo_name, avg_time in results:
            writer.writerow([size, data_type, algo_name, avg_time])

    print(f"\nResults have been successfully saved to '{csv_file}' for further analysis.\n")
