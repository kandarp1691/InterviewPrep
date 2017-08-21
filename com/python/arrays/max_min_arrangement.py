# Rearrange an array in max min form
from pdb import set_trace as bp

def rearrange_max_min(arr, n):
    new_arr = [0 for k in range(n)]
    j = n - 1
    i = 0
    idx = 0
    #bp()
    while idx < n :
        new_arr[idx] = arr[j]
        idx += 1
        if idx >= n :
            break;
        new_arr[idx] = arr[i]
        j = j - 1
        i = i + 1
        idx += 1
    print new_arr


arr = [1,2,3,4,5,6,7]
n = len(arr)
rearrange_max_min(arr,n)