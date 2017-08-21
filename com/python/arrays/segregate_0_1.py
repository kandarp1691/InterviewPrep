# This python code segregates 0 and 1


def segregate(arr, n):
    n = len(arr) - 1
    start = 0
    end = n

    while start < end:
        while arr[start] == 0 and start < end:
            start = start + 1
        while arr[end] == 1 and start < end:
            end = end - 1

        if arr[start] > arr[end]:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start = start + 1
            end = end - 1

    print arr

arr = [1,0,0,0,1,1,0,1]
n = len(arr)
segregate(arr,n)
