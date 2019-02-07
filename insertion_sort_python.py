
def insertionSort(array):
    for i in range(1, len(array)):
        select_ind = i
        for j in range(i - 1, -1, -1):
            if array[select_ind] < array[j]:
                array[j], array[select_ind] = array[select_ind], array[j]
                select_ind = j

array = [1, 4, 2, 3, 1, 0, 4, 6]
selectionSort(array)
print(array)

