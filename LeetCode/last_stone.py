# 1046. Last Stone Weight

def lastStoneWeight(stones):
    stones = sorted(stones)
    while len(stones)>= 1:
        max = stones[-1]
        smax = stones[-2]
        if max == smax:
            stones.remove(smax)
            stones.remove(max)
        else:
            diff = max - smax
            stones.append(diff)
            stones.remove(max)
            stones.remove(smax)
        stones = sorted(stones)
        if len(stones) == 0:
            return 0
    return stones[0]

print lastStoneWeight([2,2])