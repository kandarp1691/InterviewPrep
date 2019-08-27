def intersection(nums1, nums2):
    dict = {}
    res = []
    for i in nums1:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1

    for i in nums2:
        if i in dict and dict[i]>0:
            res.append(i)
            dict[i] = dict[i]-1
    return res




nums1 = [1,2]
nums2 = [1,1]
print intersection(nums1, nums2)