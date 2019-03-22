# This code sorts an array in waveform style --> {2,3,4,6}-->{3,2,6,4}


def waveform_sort(a):
    i = 0;
    n = len(a)-1
    a = sorted(a)
    while i+2 <= n:
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp
        i = i+2

    return a

a = [3,6,5,10,7,20]
print waveform_sort(a)

