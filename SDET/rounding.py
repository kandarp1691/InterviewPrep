def round_nearest(n):
    if n%10 < 5:
        n = n - n%10
        print n
    elif n%10 >= 5:
        n = n + (10 - n%10)
        print n
    else:
        print n


round_nearest(212)


