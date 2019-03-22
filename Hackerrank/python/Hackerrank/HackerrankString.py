def hackerrank_string(s):
    h_string = 'hackerrank'
    l = len(s)-1
    match_counter = 0
    i = 0
    j = 0
    if len(s) < len(h_string):
        print 'NO'
    while i<= l:
        if s[i] == h_string[j]:
            match_counter = match_counter + 1
            j= j + 1
        i = i+ 1
    if len(h_string) == match_counter:
        print 'YES'



hackerrank_string('hereiamstackerrank')