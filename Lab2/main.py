import matplotlib.pyplot as plt
from sorting import sort

if __name__ == "__main__":

    # Initialize lists to store number of elements and execution times
    n_elements = []
    exec_times = []

    # Sort the array with quickSort and record the execution time
    sort(n_elements, exec_times, "quickSort")
    print("quickSort times: ", exec_times)

    # Plot on the graph
    plt.plot(n_elements, exec_times, linewidth=3, label='quickSort')

    # Reset the lists
    n_elements = []
    exec_times = []

    # Sort the array with mergeSort and record the execution time
    sort(n_elements, exec_times, "mergeSort")
    print("mergeSort times: ", exec_times)

    # Plot on the graph
    plt.plot(n_elements, exec_times, linewidth=3, label='mergeSort')

    # Reset the lists
    n_elements = []
    exec_times = []

    # Sort the array with heapSort and record the execution time
    sort(n_elements, exec_times, "heapSort")
    print("heapSort times: ", exec_times)

    # Plot on the graph
    plt.plot(n_elements, exec_times, linewidth=3, label='heapSort')

    # Reset the lists
    n_elements = []
    exec_times = []

    # Sort the array with bucketSort and record the execution time
    sort(n_elements, exec_times, "bucketSort")
    print("bucketSort times: ", exec_times)

    # Plot the graph
    plt.plot(n_elements, exec_times, linewidth=3, label='bucketSort')
    plt.xlabel("Number of elements")
    plt.ylabel("Time, s")
    plt.title("Sorting algorithms Execution Time")
    plt.legend()
    plt.show()
