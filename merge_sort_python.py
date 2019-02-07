#merge sort

def merge(array, left, middle, right):

    left_array = array[left:middle + 1]
    right_array = array[middle + 1:right + 1]
    i = j = 0
    k = left

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1

        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1

def merge_sort(array, left, right):
    if len(array) < 1:
        return

    if left >= right:
        return array[left]

    middle = (right + left) // 2

    merge_sort(array, left, middle)
    merge_sort(array, middle + 1, right)

    merge(array, left, middle, right)



array = [5, 7, 2, 4, 1, 8, 7, 4, 4, 4]
print(array)
merge_sort(array, 0, len(array) - 1)
print(array)
