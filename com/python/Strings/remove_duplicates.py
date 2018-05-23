def remove_dups(string):
    res = set(string)
    print ''.join(res)


def remove_dupls_hashing(string):
    map = {}
    for i in string:
        if i not in map:
            map[i] = 1
    print ''.join(map)

remove_dupls_hashing('geeksforgeeks')