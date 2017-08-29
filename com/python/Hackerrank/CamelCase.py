def countWords(s):
    word_count = 0
    for char in range(0, len(s)):
        if s[char].isupper():
            word_count += 1
    if s[0].islower():
        word_count += 1
    return word_count

s = 'saveChangesInTheEditor'
print countWords(s)