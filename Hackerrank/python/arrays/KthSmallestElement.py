import heapq
def find_kth_smallest(arr, k):
    smallest = []
    for i in arr:
        if len(smallest) < k:
            heapq.heappush(smallest, -i)
        else:
            heapq.heappop(smallest, -i)
    if len(smallest) < k:
        return None
    return -smallest[0]


arr = [4, 1, 7, 8, 10, 5]
k = 3
find_kth_smallest(arr, k)
