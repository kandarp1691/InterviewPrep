def findkoccurences(arr, n):
    map = {}
    for i in arr:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    for k,v in map.iteritems():
        if map[k] == n:
            print k
arr = [1,2,3,4,1,2]
findkoccurences(arr,2)

