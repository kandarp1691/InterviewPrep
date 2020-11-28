def removeVowels(S):
    S = list(S)
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(0, len(S)):
        if S[i] in vowels:
            S[i] = ""
    return ''.join(S)

S = 'leetcodeisacommunityforcoders'
print removeVowels(S)
