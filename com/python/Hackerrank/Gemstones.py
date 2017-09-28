#Doubt
def gemstones(arr):
    set_a = set(arr[0])
    for each_string in range(1, len(arr)-1):
        for i in range(0, len(each_string)):
            if i in set_a:
                pass
