import sys
def eleshop(money, keyboards, drives):
    spent = -1
    for i in range(0, len(keyboards)):
        for j in range(0, len(drives)):
            if keyboards[i] + drives[j] <= money:
                spent = max(spent, keyboards[i] + drives[j])

    print spent


eleshop(5, [3], [4])