"""Radix sort implementation depend on input data, but logic is folowing
    below implementation for integer digits. Usually sorting digit"""

def countingSort(array, exp1):
    if len(array) < 1:
        return []
    count =[0] * 10
    output = [0] * len(array)

    for i in range(len(array)):
        count[(array[i] // exp1) % 10] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(array) - 1, -1, -1):
        ind = array[i] // exp1
        output[count[ind % 10] - 1] = array[i]
        count[ind % 10] -= 1

    for i in range(len(array)):
        array[i] = output[i]

    return count

def radixSort(array):
    exp1 = 1
    maximum = max(array)

    while maximum // exp1 > 0:
        countingSort(array, exp1)
        exp1 *= 10

array = [ 170, 45, 75, 90, 802, 24, 2, 66]
radixSort(array)
print(array)


