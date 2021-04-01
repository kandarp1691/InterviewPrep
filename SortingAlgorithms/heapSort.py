def heapsort(arr, n):
    for i in range(n/2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i, 0)
    return arr


def heapify(arr, n, i):
    largest= i
    l = 2*i
    r = 2*i + 1
    while l < n and arr[l] > arr[largest]:
        largest = l
    while r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        heapify(arr, n, largest)

arr = [6,2,4,9,1,5,8]
print heapsort(arr, 7)