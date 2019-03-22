arr = [1,2,3,4,5,6]

def rotate(arr, d):
    reverse(arr, 0, d-1)
    reverse(arr, d, len(arr)-1)
    reverse(arr, 0, len(arr)-1)
    print arr

def reverse(arr, start, end):
    while start < end :
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start +=1
        end -= 1
    return arr

rotate(arr, 3)