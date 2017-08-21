def segregate(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        if arr[start]%2 == 0:
            start += 1
        if arr[end]%2 == 1:
            end = end - 1
        else:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end = end - 1
    return arr

arr = [12,34,45,9,8,90,3]
print segregate(arr)