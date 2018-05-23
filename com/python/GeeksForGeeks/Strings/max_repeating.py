def max_repeating(string):
    dmap = {}
    for i in range(0, len(string)):
        if string[i] in dmap:
            dmap[string[i]] = dmap[string[i]] + 1
        else:
            dmap[string[i]] = 1

    return max(dmap,key=dmap.get)

string = 'test'
print max_repeating(string)