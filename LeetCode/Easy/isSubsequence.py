def isSubsequence(s,t):
    idx = 0
    nmap = {}
    for each in range(0, len(t)):
        if t[each] not in nmap:
            nmap[t[each]] = each
    for i in range(0, len(s)):
        if nmap.has_key(s[i]) and nmap[s[i]] >= idx:
            idx=nmap[s[i]]
        else:
            return False
    return True

print isSubsequence('aaaaaa', 'bbaaaa')
