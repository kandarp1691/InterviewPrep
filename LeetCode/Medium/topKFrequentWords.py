import heapq
def topKFreqWords(wrds, K):
    map = {}
    for each in wrds:
        if each in map:
            map[each] = map[each] + 1
        else:
            map[each] = 1
    ls = []
    for k, v in map.iteritems():
        heapq.heappush(ls, (k, v))
    ls = sorted(ls, key=lambda x:x[1], reverse=True)
    ans = []
    while K != 0:
        ans.append(ls.pop(0)[0])
        K = K - 1  
    return ans

print topKFreqWords(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)