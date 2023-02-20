# Heapify function to maintain the heap property of the given list
def heapify(dataList, low, high):
    largest = high
    left = 2 * high + 1    # calculate the index of the left child
    right = 2 * high + 2    # calculate the index of the right child

    # Check if the left child is larger than the highest index element
    # If so, update the largest index to the index of the left child
    if left < high and dataList[high] < dataList[left]:
        largest = left

    # Check if the right child is larger than the element at the largest index
    # If so, update the largest index to the index of the right child
    if right < high and dataList[largest] < dataList[right]:
        largest = right

    # If the largest index is not the same as the highest index, swap the elements
    # at those indices and call heapify recursively on the new largest index
    if largest != high:
        (dataList[high], dataList[largest]) = (dataList[largest], dataList[high])
        heapify(dataList, low, largest)


# Heap sort function to sort the given list of data
def heapSort(dataList):
    n = len(dataList)

    # Build a max heap by calling heapify on the bottom half of the list
    for i in range(n // 2 - 1, -1, -1):
        heapify(dataList, n, i)

    # Sort the list by repeatedly swapping the first element with the last element
    # and calling heapify to restore the heap property
    for i in range(n - 1, 0, -1):
        (dataList[i], dataList[0]) = (dataList[0], dataList[i])
        heapify(dataList, i, 0)
