def second_max(arr):
    max = 0
    smax = 0

    for i in range(0, len(arr)):
        if arr[i] > max:
            smax = max
            max = arr[i]
        else:
            if arr[i] < max and arr[i] != max:
                smax = arr[i]

    return max, smax

print second_max([1,2,3,4,5,6,7])