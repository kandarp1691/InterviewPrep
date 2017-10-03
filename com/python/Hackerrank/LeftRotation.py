def leftRotation(a, d):
    reverse(a,0,d-1)
    reverse(a,d,len(a)-1)
    reverse(a,0,len(a)-1)
    return a

def reverse(a, start, end):
    while start < end:
        temp = a[start]
        a[start] = a[end]
        a[end] = temp
        start+=1
        end = end-1
    return a

a = [1,2,3,4,5]
print leftRotation(a,4)
