def sum3(arr):
    res = []
    arr = sorted(arr)
    for i in range(len(arr)):
        if arr[i] > 0:
            break
        if i == 0 or arr[i-1] != arr[i]:
            sum(arr, i, res)
    return res

def sum(arr, i, res):
    l = i+1
    h = len(arr)-1
    while l < h:
        if arr[i] + arr[l] + arr[h] < 0:
            l=l+1
        elif arr[i] + arr[l] + arr[h] > 0:
            h = h-1
        else:
            res.append([arr[i], arr[l], arr[h]])
            l=l+1
            h = h-1
            while l<h and arr[l-1] == arr[l]:
                l = l+1

print sum3([-1,0,1,2,-1,-4])