def check_k_anagrams(str1):
    n = len(str1)
    count = []
    for i in range(0, n):
        count[ord(str[i]) - ord('a')] += 1
    print count

check_k_anagrams('anagram')