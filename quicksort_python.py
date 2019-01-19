"""sorting algorithm based on recursion
    and divide and conquer principle
    Big O notation - O(nlog n)"""

def qsort(array):

    #base case
    if len(array) < 2:
        return array

    #choose pivot element
    pivot = array[0]
    head = qsort([a for a in array[1:] if a <= pivot])
    #pivot = [a for a in array if a == pivot]
    tail = qsort([a for a in array[1:] if a > pivot])

    return head + [pivot] + tail


array = [1, 4, 2, 6, 1, 5, 2]
print(qsort(array))