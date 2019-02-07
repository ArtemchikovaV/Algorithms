"""Sorting only integer digits array [0 .. N - 1].
    Not conparison sorting algorithm.
    O(n)"""

def countingSort(array):

    if len(array) < 1:
        return []

    count = [0 for i in range(max(array) + 1)]
    output = [0 for i in range(len(array))]
    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(array)):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1

    return output


array = [3, 6, 1, 2, 3, 3, 89, 8, 2]
print(countingSort(array))
print(array)

