def bigsorting(unsorted):
    for i in range(0,len(unsorted)):
        for j in range(i, len(unsorted)):
            if unsorted[i] > unsorted[j]:
                temp = unsorted[i]
                unsorted[i] = unsorted[j]
                unsorted[j] = temp

    return unsorted

unsorted = [31415926535897932384626433832795,1,3,10,3,5]
print bigsorting(unsorted)
