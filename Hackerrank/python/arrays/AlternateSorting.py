def sort_alternate(arr):
    arr = sorted(arr)
    start = 0
    end = len(arr) - 1
    alt_arr = ''
    while start < end:
        alt_arr = alt_arr + ' ' + str(arr[end]) + ' ' + str(arr[start])
        start+=1
        end = end-1

    return alt_arr

arr = [1,6,9,4,3,7,8,2]
print sort_alternate(arr)
