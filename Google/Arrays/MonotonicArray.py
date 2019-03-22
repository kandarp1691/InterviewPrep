def isMonotonic(arr):
    if arr[0] <= arr[1]:
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                return False
        return True
    else:
        if arr[0] >= arr[1]:
            for i in range(1, len(arr)):
                if arr[i-1] < arr[i]:
                    return False
        return True

print isMonotonic([1,1,0])
