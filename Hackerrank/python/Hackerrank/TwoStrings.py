def twoStrings(s1,s2):
    cmap = {}
    x = None
    y = None
    if len(s1) >= len(s2):
        x = s1
        y = s2
    else:
        x = s2
        y = s1
    for i in range(0, len(x)):
        if x[i] in cmap:
            cmap[x[i]] += 1
        else:
            cmap[x[i]] = 1

    for i in range(0, len(y)):
        if y[i] in cmap:
            return 'YES'
            break
    return 'NO'

print twoStrings('hi', 'world')