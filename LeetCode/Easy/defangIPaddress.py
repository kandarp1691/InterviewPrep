def defang(ip):
    ans = []
    for i in range(0, len(ip)):
        if ip[i] == '.':
            ans.append('[.]')
        else:
            ans.append(ip[i])
    return ''.join(ans)

print defang('1.1.1.1')

