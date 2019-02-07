#increase bubble sort
def bubble_sort(array):

    for i in range(len(array)):
        swapped = False

        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if swapped == False:
            break


array = [2, 4, 5, 1, 3, 4, 6, 7, 0]
bubble_sort(array)
print(array)