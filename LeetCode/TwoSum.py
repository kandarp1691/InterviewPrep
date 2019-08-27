def twoSum(nums, target):
    dict = {}
    for i in range(0, len(nums)):
        d = target - nums[i]
        if d in dict:
            return (dict[d][1],i)
        else:
            dict[nums[i]] = (d, i)




nums = [3,3]
print twoSum(nums, 6)