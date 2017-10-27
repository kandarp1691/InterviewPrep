def leftRotation(a, d):
    reverse(a,0,d-1)
    reverse(a,d,len(a)-1)
    reverse(a,0,len(a)-1)
    return a

def reverse(a, start, end):
    while start < end:
        temp = a[end]
        a[end] = a[start]
        a[start] = temp
        start+=1
        end = end-1
    return a
k = 2
i = 1
a = [1,2,3]
while i <= k:
    print i
    print leftRotation(a,i)
    i +=1
