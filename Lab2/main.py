import matplotlib.pyplot as plt
from sorting import sort

if __name__ == "__main__":
    '''
    test =[]
    for i in range(1000):
        test.append(random.randint(-1000, 1000))
    print(test)
    '''

    # Initialize lists to store number of elements and execution times
    n_elements = []
    exec_times = []

    # Sort the array with quicksort and record the execution time
    sort(n_elements, exec_times, "quickSort")   # Quick Sort

    # Plot the graph
    plt.plot(n_elements, exec_times, linewidth=3, label='quickSort')

    n_elements = []
    exec_times = []

    sort(n_elements, exec_times, "mergeSort")   # Merge sort

    # Plot the graph
    plt.plot(n_elements, exec_times, linewidth=3, label='mergeSort')

    n_elements = []
    exec_times = []

    sort(n_elements, exec_times, "heapSort")  # Heap sort

    # Plot the graph
    plt.plot(n_elements, exec_times, linewidth=3, label='heapSort')

    plt.xlabel("Number of elements")
    plt.ylabel("Time, s")
    plt.title("Sorting algorithms Execution Time")
    plt.legend()
    plt.show()

    n_elements = []
    exec_times = []

    sort(n_elements, exec_times, "bubbleSort")  # Bubble sort

    # Plot the graph
    plt.plot(n_elements, exec_times, color='red', linewidth=3, label='bubbleSort')

    plt.xlabel("Number of elements")
    plt.ylabel("Time, s")
    plt.title("Bubble Sort Execution Time")
    plt.legend()
    plt.show()
