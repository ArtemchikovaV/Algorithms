

def insertionSort(array):

    for i in range(1, len(array)):
        select_ind = i
        for j in range(i - 1, -1, -1):
            if array[select_ind] < array[j]:
                array[j], array[select_ind] = array[select_ind], array[j]
                select_ind = j

def bucketSort(array):

    max_value = max(array)
    n_busket = int(max_value ** 0.5)
    buskets = [[] for _ in range(n_busket)]
    size_bucket = max_value // n_busket

    for i in range(len(array)):
        if array[i] // size_bucket != n_busket:
            buskets[array[i] // size_bucket].append(array[i])
        else:
            buskets[n_busket - 1].append(array[i])

    result = []
    for busket in buskets:
        insertionSort(busket)
        result += busket

    return result

array = [2, 3, 4, 1, 2, 3, 7, 3, 1, 10]
print(bucketSort(array))




