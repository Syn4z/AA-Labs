import matplotlib.pyplot as plt
from sorting import sort

if __name__ == "__main__":

    # Initialize lists to store number of elements and execution times
    n_elements = []
    exec_times = []

    # Sort the array with quickSort and record the execution time
    sort(n_elements, exec_times, "quickSort")

    # Plot on the graph
    plt.plot(n_elements, exec_times, linewidth=3, label='quickSort')

    # Reset the lists
    n_elements = []
    exec_times = []

    # Sort the array with mergeSort and record the execution time
    sort(n_elements, exec_times, "mergeSort")

    # Plot on the graph
    plt.plot(n_elements, exec_times, linewidth=3, label='mergeSort')

    # Reset the lists
    n_elements = []
    exec_times = []

    # Sort the array with heapSort and record the execution time
    sort(n_elements, exec_times, "heapSort")

    # Plot on the graph
    plt.plot(n_elements, exec_times, linewidth=3, label='heapSort')

    # Reset the lists
    n_elements = []
    exec_times = []

    # Sort the array with bubbleSort and record the execution time
    sort(n_elements, exec_times, "bucketSort")

    # Plot the graph
    plt.plot(n_elements, exec_times, linewidth=3, label='bubbleSort')
    plt.xlabel("Number of elements")
    plt.ylabel("Time, s")
    plt.title("Sorting algorithms Execution Time")
    plt.legend()
    plt.show()
