import sys
def closestNumbers(arr):
    map = {}
    ans = []
    arr = sorted(arr)
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        map[(arr[i-1], arr[i])] = diff
    # print map
    min_val = map[min(map, key=map.get)]
    print min_val
    for k,v in map.iteritems():
        if v == min_val:
            ans.append(k)
    print ans
    # for i in ans:
    #     res.append(i[0])
    #     res.append(i[1])
    res = sorted([x for t in ans for x in t])
    return ' '.join(str(i) for i in res)


print closestNumbers([1,2,3,4,5])