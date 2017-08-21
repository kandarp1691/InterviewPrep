# This program is a test to reverse an array


def reverse_array(array):
    start = 0
    end = len(array)-1

    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start = +1
        end = -1

    print array

array = [1,2,3,4,5]
reverse_array(array)



