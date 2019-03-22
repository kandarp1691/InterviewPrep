def bubblesort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr

arr = [3,2,9,6,5]
print bubblesort(arr)
