def super_reduced_string(s):
    map = {}
    ans = ''
    for i in range(0, len(s)):
        if s[i] in map and map[s[i]] != 0:
            map[s[i]] = map[s[i]] - 1
        else:
            map[s[i]] = 1
    for k,v in map.iteritems():
        if v==1:
            ans = ans+k
    if len(ans) > 0:
        return ans
    else:
        return 'Empty String'

s = 'aaabccddd'
print super_reduced_string(s)