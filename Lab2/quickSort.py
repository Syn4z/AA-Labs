# function to partition the input list and return the index of the pivot element
def partition(dataList, low, high):
    # set the pivot element to the last element in the list
    pivot = dataList[high]

    # set the starting index for elements that are greater than the pivot
    i = low - 1

    # loop through the list from low to high
    for j in range(low, high):
        # if the current element is less than or equal to the pivot
        if dataList[j] <= pivot:
            # move the element to the left side of the pivot
            i = i + 1
            (dataList[i], dataList[j]) = (dataList[j], dataList[i])

    # move the pivot to its correct position
    (dataList[i + 1], dataList[high]) = (dataList[high], dataList[i + 1])

    # return the index of the pivot element
    return i + 1


# function to implement quicksort algorithm
def quickSort(dataList, low, high):
    # if there are more than one element in the list
    if low < high:
        # partition the list and get the index of the pivot
        pi = partition(dataList, low, high)

        # recursively call quicksort on the left side of the pivot
        quickSort(dataList, low, pi - 1)

        # recursively call quicksort on the right side of the pivot
        quickSort(dataList, pi + 1, high)
