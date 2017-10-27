def check_funny_string(string):
    s1 = string
    s2 = ''.join(reversed(string))
    flag = False

    for i in range(1, len(s1)):
        print i
        if abs(ord(s1[i]) - ord(s1[i-1])) == abs(ord(s2[i]) - ord(s2[i-1])):
            print ord(s1[i]), ord(s1[i-1]), ord(s2[i]), ord(s2[i-1])
            flag = True
        else:
            flag = False
            break
    if flag is True:
        print 'Funny'
    else:
        print 'Not Funny'

check_funny_string('ivvkx')
