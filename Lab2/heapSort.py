# This function arranges the elements of an array into a heap
# It takes three arguments: the array, its size, and the index of the element to start heapify from
def heapify(dataList, n, i):
    largest = i    # initialize the index of the largest element as i
    left = 2 * i + 1    # get the index of the left child of the element at i
    right = 2 * i + 2    # get the index of the right child of the element at i

    # If the left child of i is larger than the largest element so far, update the largest index
    if left < n and dataList[left] > dataList[largest]:
        largest = left

    # If the right child of i is larger than the largest element so far, update the largest index
    if right < n and dataList[right] > dataList[largest]:
        largest = right

    # If the largest element is not i, swap the i-th and largest elements and recursively heapify the affected subtree
    if largest != i:
        dataList[i], dataList[largest] = dataList[largest], dataList[i]
        heapify(dataList, n, largest)


def heapSort(dataList):
    n = len(dataList)

    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(dataList, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        dataList[0], dataList[i] = dataList[i], dataList[0]
        heapify(dataList, i, 0)

    return dataList
