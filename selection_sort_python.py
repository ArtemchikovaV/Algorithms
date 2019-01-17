"""selection sort algorithm for an array"""

def findIndOfMinimum(array):

    minimum = array[0]
    min_ind = 0

    for i in range(len(array)):
        if array[i] < minimum:
            minimum = array[i]
            min_ind = i

    return min_ind


def findIndOfMaximum(array):

    maximum = array[0]
    max_ind = 0

    for i in range(len(array)):
        if array[i] > maximum:
            maximum = array[i]
            max_ind = i

    return max_ind


def selectionSort(array, reverse=0):

    """if reverse = 1 sorting in descending order"""
    new_array = [0 for i in range(len(array))]

    if reverse == 0:
        for i in range(len(array)):
            min_ind = findIndOfMinimum(array)
            new_array[i] = array.pop(min_ind)
    else:
        for i in range(len(array)):
            max_ind = findIndOfMaximum(array)
            new_array[i] = array.pop(max_ind)

    return new_array

"""initial array will be delete during the selection sorting"""
array = [1, 5, 2, 10, 0, 2, 10, 3]
print(selectionSort(array))
print(selectionSort(array, 1))

array = [1, 5, 2, 10, 0, 2, 10, 3]
array = selectionSort(array, 1)
print(array)
print(selectionSort(array))
