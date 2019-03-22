arr = [1,2,3,4,5,1,1,3,4,6,8,9]

def find_duplicates(arr):
    res = {}
    for i in range(0, len(arr)):
        if arr[i] in res:
            res[arr[i]] = res[arr[i]] + 1
        else:
            res[arr[i]] = 1
    print res


def print_only_dups(arr):
    res = {}
    for i in range(0, len(arr)):
        if arr[i] in res:
            res[arr[i]] = res[arr[i]] + 1
        else:
            res[arr[i]] = 1
    for k,v in res.iteritems():
        if v > 1:
            print str(k) + " " + str(res[k])




print_only_dups(arr)