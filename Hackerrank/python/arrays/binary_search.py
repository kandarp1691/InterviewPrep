# Binary Search Alogorithm assuming the array is sorted
def binary_search(key, arr, min, max):
    mid = int((max + min)/2)

    if max < min:
        return -1

    if key > arr[mid]:
        return binary_search(key, arr, mid+1, max)
    if key < arr[mid]:
        return binary_search(key, arr, min, mid-1)
    else:
        return mid

arr = [1,4,6,8,11,14,15,24]

binary_search(14, arr, 0, len(arr)-1)