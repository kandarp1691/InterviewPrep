# This python program will rotate array one by one


def rotate_one(arr):
    length = len(arr)-1
    temp = arr[length]

    re_len = length
    while re_len != 0:
        arr[re_len] = arr[re_len - 1]
        re_len = re_len - 1

    arr[0] = temp

    print arr

arr = [1,2,3,4,5]
rotate_one(arr)
