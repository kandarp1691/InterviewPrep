#283. Move Zeroes

def moveZeroes(nums):
    i = 0
    j = len(nums)-1

    while i < j:
        if nums[i] != 0:
            i += 1
        if nums[j] == 0:
            j -=1
        else:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i+=1
            j-=1
    return nums

def moveZeroesMaintainOrder(nums):
    j = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            j+=1
    return nums


print moveZeroesMaintainOrder([0,1,0,3,12])