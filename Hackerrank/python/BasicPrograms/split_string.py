def split_string(str):
    split_s = [];
    tmp = ''
    for i in str:
        if i == ' ':
            split_s.append(tmp)
            tmp = ''
        else:
            tmp = tmp + i
    if tmp :
        split_s.append(tmp)
    print split_s

str = 'this is a sentence'
split_string(str)
