def solve(n,p):
    count_f = 0.5
    count_b = 0.5
    j = n-1
    i = 1
    while i != p:
        count_f += 0.5
        i += 1

    while j != p:
        count_b += 0.5
        j = j-1
    return min(int(count_b), int(count_f))

print solve(5,4)

