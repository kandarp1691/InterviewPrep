def quicksort(arr):
    quicksort_helper(arr, 0, len(arr)-1)
    return arr


def quicksort_helper(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        print pivot
        print arr
        quicksort_helper(arr, left, pivot-1)
        quicksort_helper(arr, pivot+1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i = i+1
            swap(arr, i, j)
    swap(arr, i+1, right)
    return i+1


def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp

quicksort([3,8,7,1,5,6])