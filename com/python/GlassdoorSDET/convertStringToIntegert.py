def convert_string_to_integer(str):
    res = 0
    sign = 1
    if str[0] == '-':
        sign = -1
        str = str[1:]

    for each_ch in str:
        res = res*10 + ord(each_ch)-ord('0');

    return sign*res

print convert_string_to_integer('123')