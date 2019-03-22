import copy
def remove_duplicates(arr):
    j = 0
    i = 1
    while i < len(arr):
        if arr[i] == arr[j]:
            i = i+1
        else:
            j=j+1
            arr[j] = arr[i]
            i=i+1
    new_arr = arr[0:j+1]
    print new_arr


arr = [1,1,2,2,3]
remove_duplicates(arr)

