def kangaroojump(x1,v1,x2,v2):
    d1 = x1 + v1
    d2 = x2 + v2
    i=0
    ans = ''
    while d1 != d2:
        d1 = d1 + v1*i
        d2 = d2 + v2*i
        if d1 == d2:
            ans =  'YES'
        else:
            ans = 'NO'
        i += 1
    return ans
print kangaroojump(0,2,5,3)