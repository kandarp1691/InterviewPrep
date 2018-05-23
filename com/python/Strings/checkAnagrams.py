def check_anagram(str1, str2):
    dmap = {}
    for i in str1:
        if i in dmap:
            dmap[i] = dmap[i]+1
        else:
            dmap[i] = 1
    for j in str2:
        if j in dmap:
            dmap[j] = dmap[j]-1
    for k in dmap:
        if dmap[k] != 0:
            print 'Not anagram'

check_anagram('geeks', 'geeks')