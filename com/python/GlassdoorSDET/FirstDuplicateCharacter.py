def find_first_repeating(word):
    map = {}
    for i in range(0, len(word)):
        if word[i] in map:
            return word[i]
        else:
            map[word[i]]=1

word = 'xyzabcaxy'
print find_first_repeating(word)