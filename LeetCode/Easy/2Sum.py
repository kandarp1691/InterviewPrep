def sum2(arr, target):
    l = 0
    r = len(arr)-1
    res = []

    while l < r:

        s = arr[l]+arr[r]
        if s == target:
            return (l+1, r+1)
        if s > target:
            r=r-1
        if s < target:
            l=l+1
    return (-1,-1)

print sum2([2,7,11,15], 9)