# This code returns the character occuring maximum time in a String

def maxOccChar(word):
    count = {}
    for i in word:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1
    max = 0
    char = ''
    for j in count:
        if max < count[j]:
            max = count[j]
            char = str(j)

    return str(max) + " " + str(char)

print maxOccChar("abracadabra")

