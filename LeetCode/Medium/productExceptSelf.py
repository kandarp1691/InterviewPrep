def productExceptSelf(arr):
    map = {}
    for i in range(0, len(arr)):
        map[i] = arr[i]
    print map
    for i in range(0, len(arr)):
        prod = 1
        for k,v in map.iteritems():
            if k != i:
                prod = prod * map[k]
        arr[i] = prod
    return arr

print productExceptSelf([1,2,3,4])