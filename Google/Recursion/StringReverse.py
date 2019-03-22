def reverseString(word):
    n = len(word)
    if len(word) == 1:
        return word
    else:
        return reverseString(word[1:n]) + word[0]

print reverseString('kandarp')