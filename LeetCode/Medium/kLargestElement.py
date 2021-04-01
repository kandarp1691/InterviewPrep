import heapq
def findKthLargest(arr, k):
    return heapq.nsmallest(k, arr)

l = [3,2,1,5,6,4]
k = 2
print findKthLargest(l,2)