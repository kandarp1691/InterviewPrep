def timeConversion(s):
    result = ''
    # Complete this function
    if s[len(s) - 2:len(s)] == 'PM':
        s = s[0:len(s) - 2]
        s_arr = s.split(":")
        if int(s_arr[0]) + 12 >=24:
            s_arr[0] = str(s_arr[0])
        else:
            s_arr[0] = str(int(s_arr[0]) + 12)
        result = ":".join(s_arr)
    elif s[len(s)-2:len(s)] == 'AM':
        s = s[0:len(s) - 2]
        s_arr = s.split(":")
        if s_arr[0] == '12':
            s_arr[0] = '00'
        result = ':'.join(s_arr)

    print result

s = "12:05:45PM"
timeConversion(s)