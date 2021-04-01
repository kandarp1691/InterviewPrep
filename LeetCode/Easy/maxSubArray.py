def maxSubArray(nums):
    maxSum = nums[0]
    sum = nums[0]
    for i in range(1, len(nums)):
        sum = max(nums[i] + sum, nums[i])
        maxSum = max(sum, maxSum)
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print maxSubArray(nums)