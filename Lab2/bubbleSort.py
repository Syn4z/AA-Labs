def bubbleSort(dataList):
    n = len(dataList)    # get the length of the input array

    for i in range(n):    # outer loop to run n times
        for j in range(0, n - i - 1):    # inner loop to compare adjacent elements

            # check if the current element is greater than the next element
            if dataList[j] > dataList[j + 1]:
                # if yes, swap the elements using tuple assignment
                dataList[j], dataList[j + 1] = dataList[j + 1], dataList[j]
