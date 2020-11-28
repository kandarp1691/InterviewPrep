def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
    print nums
nums = [1,1,1,1,1]
runningSum(nums)