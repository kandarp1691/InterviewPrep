def alternate_characters(s):
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count+=1
    if count == 0:
        return 0
    return count

print alternate_characters('ABCDAAAA')