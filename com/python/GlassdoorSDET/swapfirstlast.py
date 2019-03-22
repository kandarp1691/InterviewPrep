def swap(str):
    words = str.split(" ")
    for i in range(0, len(words)):
        words[i] = interchange(words[i])
    return " ".join(words)


def interchange(word):
    l = 0
    r = len(word)-1
    new_word = word[r] + word[1:r] + word[l]
    return new_word

print swap('geeks for geeks')