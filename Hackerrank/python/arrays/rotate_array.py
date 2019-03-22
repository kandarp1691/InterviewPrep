# Python program to rotate an array where d is the degree of rotation


def rotate_array(array, d):
    n = len(array) - 1
    reverse_array(array, 0, d-1)
    print array
    reverse_array(array, d, n)
    print array
    reverse_array(array, 0, n)
    print array


def reverse_array(array, start, end):
    #start = 0
    #end = len(array) - 1

    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end = end-1

    return array

array = [1,2,3,4,5,6,7]
rotate_array(array, 3)