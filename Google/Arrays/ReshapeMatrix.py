def reshapematrix(nums, r, c):
    if len(nums) == 0:
        return nums
    arrsize = len(nums) * len(nums[0])
    resized = r * c
    if resized != arrsize:
        return nums

    flat_list = []
    for i in range(0, len(nums)):
        for j in range(0, len(nums[i])):
            flat_list.append(nums[i][j])
    ol = []
    i = 0
    while len(ol) != r:
        il = []
        while len(il) != c:
            il.append(flat_list[i])
            i = i+1
        ol.append(il)

    return ol

print reshapematrix([[1,2],[3,4],[5,6]], 3, 2)