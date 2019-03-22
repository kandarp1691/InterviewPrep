def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        element = arr[i]
        while j > 0 and arr[j-1] > element:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = element
    return arr

arr = [23,42,4,16,8,15]
print insertion_sort(arr)