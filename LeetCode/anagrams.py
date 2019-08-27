#242. Valid Anagram

def isAnagram(s,t):
    m1 = getMap(s)
    m2 = getMap(t)
    return m1==m2

def getMap(word):
    dict = {}
    for i in word:
        if i in dict:
            dict[i] = dict[i]+1
        else:
            dict[i] = 1
    return dict

print isAnagram('anagram', 'nagaram')