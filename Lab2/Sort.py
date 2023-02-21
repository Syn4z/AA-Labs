from quickSort import quickSort
from mergeSort import mergeSort
from heapSort import heapSort
from bucketSort import bucketSort


class Sort:

    def __init__(self, data, low, high):
        self.data = data
        self.low = low
        self.size = high

    def quickSort(self):
        return quickSort(self.data, self.low, self.size - 1)

    def mergeSort(self):
        return mergeSort(self.data, self.low, self.size - 1)

    def heapSort(self):
        return heapSort(self.data)

    def bucketSort(self):
        return bucketSort(self.data)
