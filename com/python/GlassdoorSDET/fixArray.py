def fix(arr):
    for i in range(0,len(arr)):
        if arr[i] != i and arr[i] != -1:
            x = arr[i]
            print x
            while arr[x] != x and arr[x] != -1:
                y = arr[x]
                print 'a[x] here is ' + str(arr[x])
                arr[x] = x
                x = y
            arr[x] = x
            print 'a[x] for this is ' + str(arr[x])
            if arr[i] != i:
                arr[i] = -1
    print arr

A = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
fix(A)