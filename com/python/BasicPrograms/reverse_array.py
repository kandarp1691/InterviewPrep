def reverse_m1(arr):
    print arr[::-1]


def reverse_m2(arr):
    res = []
    n = len(arr)
    for i in range(len(arr)-1, -1, -1):
        res.append(arr[i])
    print res


def reverse_m3(arr):
    i=0
    j=len(arr)-1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i = i + 1
        j = j - 1

    print arr

arr = [1,2,3,4]
reverse_m3(arr)