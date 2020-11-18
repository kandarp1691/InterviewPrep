def funct(string_list, q_list):
    smap = {}
    for i in range(0, len(string_list)):
        if string_list[i] in smap:
            smap[string_list[i]] += 1
        else:
            smap[string_list[i]] = 1
    print smap

    for j in range(0, len(q_list)):
        if q_list[j] in smap:
            print smap[q_list[j]]
        else:
            print 0

string_list = ['aba', 'baba', 'aba', 'xzxb']
q_list = ['aba', 'xzxb', 'ab']

funct(string_list, q_list)