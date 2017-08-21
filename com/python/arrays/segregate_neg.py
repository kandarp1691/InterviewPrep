# This program segregates negative and positive values


def move_ne(arr, n):
    temp = [0 for k in range(n)]
    j = 0
    for i in range(n):
        if arr[i] >= 0:
            temp[j] = arr[i]
            j = j+1

    if j == n or j==0:
        return

    for i in range(n):
        if arr[i] < 0:
            temp[j] = arr[i]
            j=j+1

    for k in range(n):
        arr[k] = temp[k]
    print arr
arr = [1,2,-3,-4,6,8,-10]
n = len(arr)
move_ne(arr, n)
