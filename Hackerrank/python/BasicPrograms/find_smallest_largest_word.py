def find_smallest_largest(str):
    split_str = str.split(" ");
    s = 1000;
    l = 0;
    smallest = split_str[0]
    largest = split_str[0]
    print split_str
    for i in range(0, len(split_str)):
        if len(split_str[i]) < s:
            smallest = split_str[i]
            s = len(smallest)
        if len(split_str[i]) > l:
            largest = split_str[i]
            l = len(largest)

    print smallest
    print largest

find_smallest_largest("this rhinocernos is a sentence")
