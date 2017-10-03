'''
Given an array arr[] of n integers, construct a Product Array prod[]
(of same size) such that prod[i] is equal to the product of all the elements of arr[] except arr[i].
'''


def product_array(arr):
    prod_arr = []
    product = 1
    for i in range(0, len(arr)):
        product = product * arr[i]
    for i in range(0, len(arr)):
        arr[i] = product/arr[i]

    return arr

arr = [10,3,5,6,2]
print product_array(arr)