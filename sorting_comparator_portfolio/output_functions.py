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
