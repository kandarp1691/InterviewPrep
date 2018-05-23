def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        hmap = {}
        for i in range(0, len(s1)):
            if s1[i] in hmap:
                hmap[s1[i]] = hmap[s1[i]]+1
            else:
                hmap[s1[i]] = 1
        for i in range(0, len(s2)):
            if s2[i] in hmap:
                hmap[s2[i]] = hmap[s2[i]]-1
            else:
                hmap[s2[i]]=1
        for i in hmap:
            if hmap[i] != 0:
                return False
            else:
                return True


def areAnagram(str1, str2):
    # Create two count arrays and initialize all values as 0
    count1 = [0] * 256
    count2 = [0] * 256

    # For each character in input strings, increment count
    # in the corresponding count array
    for i in str1:
        count1[ord(i)] += 1

    for i in str2:
        count2[ord(i)] += 1

    # If both strings are of different length. Removing this
    # condition will make the program fail for strings like
    # "aaca" and "aca"
    if len(str1) != len(str2):
        return 0
    print count1


    # Compare count arrays
    for i in xrange(256):
        if count1[i] != count2[i]:
            return 0

    return 1

s1 = 'abcd'
s2 = 'csbd'

print areAnagram(s1,s2)