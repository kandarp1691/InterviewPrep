def shuffle(nums, n):
    ans = []
    i = 0
    while i+n != len(nums):
        ans.append(nums[i])
        ans.append(nums[i+n])
        i = i+1
    return ans

print shuffle([2,5,1,3,4,7], 3)