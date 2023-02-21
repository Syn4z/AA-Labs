def heapify(dataList, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and dataList[left] > dataList[largest]:
        largest = left

    if right < n and dataList[right] > dataList[largest]:
        largest = right

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
