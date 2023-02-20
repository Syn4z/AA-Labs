# function to merge two sub-arrays of the input list
def merge(dataList, low, m, high):
    # calculate the lengths of the two sub-arrays
    n1 = m - low + 1
    n2 = high - m

    # create temporary arrays to store the two sub-arrays
    L = [0] * n1
    R = [0] * n2

    # copy data into the temporary arrays
    for i in range(0, n1):
        L[i] = dataList[low + i]

    for j in range(0, n2):
        R[j] = dataList[m + 1 + j]

    # merge the two sub-arrays into the input list
    i = 0
    j = 0
    k = low

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            dataList[k] = L[i]
            i += 1
        else:
            dataList[k] = R[j]
            j += 1
        k += 1

    # copy any remaining elements from the left subarray
    while i < n1:
        dataList[k] = L[i]
        i += 1
        k += 1

    # copy any remaining elements from the right subarray
    while j < n2:
        dataList[k] = R[j]
        j += 1
        k += 1


# function to implement mergesort algorithm
def mergeSort(dataList, low, high):
    if low < high:
        # find the middle point to divide the list into two halves
        m = low + (high - low) // 2

        # recursively call mergeSort on the left half of the list
        mergeSort(dataList, low, m)

        # recursively call mergeSort on the right half of the list
        mergeSort(dataList, m + 1, high)

        # merge the two sorted sub-arrays
        merge(dataList, low, m, high)
