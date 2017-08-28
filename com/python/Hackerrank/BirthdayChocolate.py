def solve(n, s, d, m):
    count = 0
    for i in range(0,n-m,1):
        if sum(s[i:i+m]) == d:
            print i,i+m
            count += 1
    return count

n = 5
s = [1,2,1,3,2]
d = 3
m = 2

print solve(n,s,d,m)