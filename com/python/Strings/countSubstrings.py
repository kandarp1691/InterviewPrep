def count_substrings(str):
    x = len(str)-1
    for i in range(0, len(str)):
        if str[i] == str[x]:
            print str[i:x]
        x=x-1

count_substrings("abcab")

