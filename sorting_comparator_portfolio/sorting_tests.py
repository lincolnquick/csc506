import time

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