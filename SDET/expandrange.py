def expand(string):
    result = []
    values = string.split(",")
    for i in range(0, len(values)):
        if '-' in values[i]:
            segment = values[i]
            numbers = segment.split("-")
            first = int(numbers[0])
            last = int(numbers[1])
            for i in range(first, last+1):
                result.append(i)
        else:
            result.append(int(values[i]))
    print result

x = '1-5,8,20,21-23'
expand(x)


