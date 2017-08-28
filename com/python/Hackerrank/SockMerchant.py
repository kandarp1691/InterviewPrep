def sockMerchant(n, ar):
    total = 0
    count = {}
    for i in range(0,n):
        if ar[i] in count:
            del count[ar[i]]
            total += 0.5
        else:
            count[ar[i]] = 0.5
    return int(total*2)

ar = [10,20,20,10,10,30,50,10,20]
print sockMerchant(len(ar), ar)
