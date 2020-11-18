def save_prisoner(n,m,s):
    count = 0


    if s < n:
        for i in range(s,n):
            count += 1
            if count == m:
                print i



save_prisoner(5,2,4)