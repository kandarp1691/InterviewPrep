def firstUniqueChar(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1

    for i in arr:
        if i in dict and dict[i] == 1:
            return arr.index(i)
    return -1

print firstUniqueChar('loveleetcode')