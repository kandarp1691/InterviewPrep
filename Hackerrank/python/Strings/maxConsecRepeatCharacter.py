def max_repeat(str):
    max = 1
    count = 1
    char = ''
    for i in range(1, len(str)):
        if str[i] == str[i-1]:
            count += 1
            c = str[i]
        else:
            count = 1
            #print str[i]
        if count > max:
            max = count
                #print max
    return max, c

str = "geeeekkks"
print max_repeat(str)

