def bucketSort(dataList, bucket_size=5):
    if len(dataList) == 0:
        return dataList

    # determine minimum and maximum values in the array
    min_value, max_value = min(dataList), max(dataList)

    # determine the number of buckets to create
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # assign each element to the appropriate bucket
    for value in dataList:
        index = (value - min_value) // bucket_size
        buckets[index].append(value)

    # sort each bucket using another sorting algorithm
    for bucket in buckets:
        bucket.sort()

    # concatenate the sorted buckets and return the result
    sorted_array = [value for bucket in buckets for value in bucket]
    return sorted_array
