def theLoveLetterMystery(s):
    l = 0;
    r = len(s)-1
    counter = 0
    while l < r:
        if ord(s[l]) != ord(s[r]):
            counter = counter + abs(ord(s[l]) - ord(s[r]))
        l = l+1
        r = r-1

    return counter

print theLoveLetterMystery('cba')
