def find_kth_smallest(arr, k):
    n = len(arr)
    arr = sorted(arr)
    print arr[k-1]

arr = [4,1,7,8,10,5]
k = 3
find_kth_smallest(arr,k)


