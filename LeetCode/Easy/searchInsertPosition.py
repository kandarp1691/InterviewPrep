def searchInsert(arr, t):
    l = 0
    r = len(arr)-1
    while l < r:
        mid = (l+r)/2
        if arr[mid] == t:
            return mid
        elif arr[mid] > t:
            r = r-1
        else:
            l = l+1
    return l

print searchInsert([1,3,5,6], 5)