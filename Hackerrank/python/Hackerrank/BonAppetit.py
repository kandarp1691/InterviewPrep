def bonAppetit(n, k, b, ar):
    # Complete this function
    sum = 0
    total = 0
    for i in range(0,n):
        total += ar[i]
    b_1 = total/2
    if b==b_1:
        print "Bon Appetit"
    else:
        sum = total - ar[k]
        b_2 = sum/2
        print b_1 - b_2
