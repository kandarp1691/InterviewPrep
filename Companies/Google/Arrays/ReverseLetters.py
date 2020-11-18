# Given
# a
# string
# S,
# return the
# "reversed"
# string
# where
# all
# characters
# that
# are
# not a
# letter
# stay in the
# same
# place, and all
# letters
# reverse
# their
# positions.
#
# Example
# 1:
#
# Input: "ab-cd"
# Output: "dc-ba"


def reverseLetters(S):
    """
    :type S: str
    :rtype: str
    """
    i = 0
    j = len(S) - 1
    S = list(S)
    while i <= j:
        if not S[i].isalpha():
            print S[i]
            i = i + 1
        if not S[j].isalpha():
            print S[j]
            j = j - 1
        if S[i].isalpha() and S[j].isalpha():
            temp = S[i]
            S[i] = S[j]
            S[j] = temp
            i = i + 1
            j = j - 1

    return ''.join(S)

print reverseLetters('7_28]')