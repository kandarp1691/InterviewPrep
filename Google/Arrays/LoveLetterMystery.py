def findMinToPal(word):
    map = {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0, len(alpha)):
        map[alpha[i]] = ord(alpha[i])
    counter = 0
    l = 0
    r = len(word)-1
    while l <= r:
        if word[l] != word[r]:
            counter = abs(ord(word[l]) - ord(word[r])) + counter
        r = r - 1
        l = l + 1
    return counter

word = 'cba'
print findMinToPal(word)
