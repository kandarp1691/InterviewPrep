def buySellStocks(prices):
    if len(prices) <= 0:
        return 0
    minSoFar = prices[0];
    diff = 0
    for i in range(1, len(prices)):
        if prices[i] < minSoFar:
            minSoFar = prices[i]
        else:
            diff = max(prices[i] - minSoFar, diff)
    return diff