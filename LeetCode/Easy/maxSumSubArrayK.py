def maxSumSubArrayK(arr, k):
    n = len(arr)
    if k > n:
        return -1
    sum_initial = 0
    for i in range(0, k):
        sum_initial = sum_initial+arr[i]

    curr_sum = sum_initial
    for i in range(k, len(arr)):
        curr_sum = curr_sum + arr[i] + arr[i-k]
        sum_initial = max(sum_initial, curr_sum)

    return sum_initial

