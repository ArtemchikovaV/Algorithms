"""binary searching algorithm for sorted array
    Big O notation - O(lon n)"""

def binary_search(array, left, right, X):

    # Element is not present in the array
    if right < left:
        return None

    mid = (left + right) // 2

    if array[mid] == X:
        return mid

    if array[mid] < X:
        return binary_search(array, mid + 1, right, X)
    elif array[mid] > X:
        return binary_search(array, left, mid - 1,  X)


def binary_search_reqursion(array, X):

    return binary_search(array, 0, len(array) - 1, X)


def binary_search_function(array, X):

    left = 0
    right = len(array) - 1

    while(left <= right):
        mid = (left + right) // 2

        if array[mid] == X:
            return mid

        if array[mid] < X:
            left = mid + 1

        elif array[mid] > X:
            right = mid - 1

    return None


array = [1, 3, 5, 6, 7, 8, 10]

print(binary_search_reqursion(array, 6))
print(binary_search_function(array, 6))
print(binary_search_reqursion(array, 1))
print(binary_search_function(array, 1))
print(binary_search_reqursion(array, 10))
print(binary_search_function(array, 10))
print(binary_search_reqursion(array, 11))
print(binary_search_function(array, 11))


