def maxSumSubarray(arr):
    max_sum_ending_here = 0
    max_sum_so_far = 0
    for i in range(0, len(arr)):
        max_sum_ending_here= arr[i] + max_sum_ending_here
        if max_sum_ending_here > max_sum_so_far:
            max_sum_so_far = max_sum_ending_here

        if max_sum_ending_here < 0:
            max_sum_ending_here = 0

    return max_sum_so_far

arr = [-2,-3,4,-1,-2,1,5,-3]
print maxSumSubarray(arr)
