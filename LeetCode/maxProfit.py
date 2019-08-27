#122. Best Time to Buy and Sell Stock II

def maxProfit(nums):
    profit = 0
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            profit = profit + (nums[i]-nums[i-1])

    print profit

maxProfit([1,2,3,4,5])