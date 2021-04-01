import heapq
def getStrongest(arr, k):
    heap = []
    res = []
    arr = sorted(arr)
    m = arr[(len(arr)-1)/2]
    for i in range(0, len(arr)):
        diff = abs(arr[i] - m)
        heapq.heappush(heap, (diff, arr[i]))
        if len(heap) > k:
            heapq.heappop(heap)
    for j in heap:
        res.append(j[1])
    return res

arr = [6,7,11,7,6,8]
print getStrongest(arr, 5)
