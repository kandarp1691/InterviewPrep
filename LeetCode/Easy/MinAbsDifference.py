import sys
def minAbsDifference(arr):
    arr = sorted(arr)
    ans = []
    minDiff = sys.maxint
    a = 0
    b = 0
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i-1]) < minDiff:
            a = arr[i-1]
            b = arr[i]
            minDiff = arr[i] - arr[i-1]
            if len(ans) != 0:
                del ans[:]
            ans.append([a,b])
        elif abs(arr[i] - arr[i-1]) == minDiff:
            a = arr[i-1]
            b = arr[i]
            ans.append([a,b])

    return ans

print minAbsDifference([-17,46,63,81,-101,-91,121,-2,112,-15,-65,-96,6,-139])