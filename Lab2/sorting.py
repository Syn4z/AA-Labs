import time
from Sort import Sort
import random
import math

random.seed(123)

data = [random.randint(-10000, 10000) for i in range(100000)]
stepList = [math.floor((i + 1) * 100000 / 20) + 1 for i in range(20)]


def sort(n_elements, exec_times, sortType):
    for i in stepList:
        start_time = time.perf_counter()
        s1 = Sort(data[:i], 0, i - 1)
        match sortType:
            case "quickSort":
                s1.quickSort()
            case "mergeSort":
                s1.mergeSort()
            case "heapSort":
                s1.heapSort()
            case "bucketSort":
                s1.bucketSort()
        end_time = time.perf_counter()

        # Append number of elements and execution time to their respective lists
        n_elements.append(i)
        exec_times.append(end_time - start_time)

    return n_elements, exec_times
