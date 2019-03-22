arr = [1,0,1,0,1,0,0]

def rearrange(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        while arr[i] == 1 and i < j:
            i = i + 1
        while arr[j] == 0 and i < j:
            j = j - 1
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i = +1
            j = -1
    print arr

rearrange(arr)

