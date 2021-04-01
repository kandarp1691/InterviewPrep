def disappearedNums(arr):
    nmap = {}
    ans = []
    for i in range(0, len(arr)):
        if arr[i] in nmap:
            nmap[arr[i]] = nmap[arr[i]] + 1
        else:
            nmap[arr[i]] = 1
    for i in range(0, len(arr)):
        if i+1 not in nmap:
            ans.append(i+1)

    return ans

def disappeared2(arr):
    for i in range(len(arr)):
        new_i = abs(arr[i])-1
        print new_i
        if arr[new_i] > 0:
            arr[new_i] = arr[new_i]*-1
    res = []
    for i in range(1, len(arr)+1):
        if arr[i-1] > 0:
            res.append(i)
    return res
arr = [4,3,2,7,8,2,3,1]

print disappeared2(arr)