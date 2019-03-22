def gridsearch(P, G):
    r = len(P)
    c = len(P[0])
    R = len(G)
    C = len(G[0])
    i = 0
    j = 0

    while i+r <= R:
        j = 0
        while j+c <= C:
            ans = [l[j:j+c] for l in G[i:i+r]]
            if ans == P:
                return 'YES'
            j = j+1
        i = i+1
    return 'NO'




G = [[1,2,3,4,5,6,7,8,9,0],[0,9,8,7,6,5,4,3,2,1], [1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1], [2,2,2,2,2,2,2,2,2,2]]
P = [[8,7,6,5,4,3], [1,1,1,1,1,1], [1,1,1,1,1,1]]

print gridsearch(P,G)
