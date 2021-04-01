import math
import heapq
def kClosestToOrigin(points, k):
    ans = []
    distances = []
    for each in points:
            x = math.sqrt(each[0]**2 + each[1]**2)
            heapq.heappush(distances, (x, each))
    print distances
    while k != 0:
        ans.append(heapq.heappop(distances)[1])
        k = k - 1
    return ans

