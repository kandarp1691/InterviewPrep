def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp

    return arr

arr = [23,42,4,16,8,25]
print selection_sort(arr)