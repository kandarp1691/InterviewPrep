def mirror(str, n):
    set = 'abcdefghijklmnopqrstuvwxyz'
    map = {}
    l = 0
    r = len(set)-1
    while r != 0:
        map[set[l]] = set[r]
        l = l+1
        r = r-1
    new_str = str[0:n-1]
    remain = str[n-1:]
    for i in range(0, len(remain)):
        new_str = new_str + map[remain[i]]
    print new_str

str = "paradox"
mirror(str, n)




