def reverse(string):
    res = ''
    for i in range(len(string), 0, -1):
        res = res + string[i-1]
    return res

def reverse_array(str):
    left = 0
    right = len(str)-1
    while left < right:
        temp = str[left]
        str[left] = str[right]
        str[right] = temp
        left += 1
        right -= 1
    print str

def reverse_string(str):
    res = ''
    print len(str)
    for i in range(len(str)-1, -1, -1):
        res = res + str[i]
    print res

reverse_string('kandarp')