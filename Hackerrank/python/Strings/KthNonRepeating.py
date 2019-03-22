def kth_non_repeating(String,k ):
    dmap = {}
    for i in String:
        if i in dmap:
            dmap[i] = dmap[i] + 1
        else:
            dmap[i] = 1

    for i in String:
        if dmap[i] == 1:
            k = k - 1
            if k == 0:
                print i


kth_non_repeating('abcdddefgh', 4)

