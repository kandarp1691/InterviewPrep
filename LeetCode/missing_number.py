# 268. Missing Number

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    max = -1
    for i in nums:
        sum = sum + i
        if i > max:
            max = i
    ideal_sum = len(nums)*(len(nums)+1)/2
    return ideal_sum-sum

print missingNumber([9,6,4,2,3,5,7,0,1])