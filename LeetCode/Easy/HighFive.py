import heapq


def highFive(items):
    res = []
    nmap = {}
    for each in items:
        if each[0] in nmap:
            heapq.heappush(nmap[each[0]], -1*each[1])
        else:
            nmap[each[0]] = [-1*each[1]]
    for k, v in nmap.iteritems():
        sum = 0
        for each in xrange(5):
            sum = sum + (heapq.heappop(v))*-1
        res.append([k, sum/5])
    return res

print highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])
