from collections import Counter
def shortestCompletingWord(licensePlate, words):
    licensePlate = licensePlate.lower()
    dic = {}
    for strings in licensePlate:
        if strings.isalpha():
            if strings not in dic:
                dic[strings] = 1
            else:
                dic[strings] += 1
    tmpdic = dic.copy()
    minlens = 1001
    ans = ""
    for i in words:
        tmpdic = dic.copy()
        count = len(tmpdic)
        for s in i:
            if s in tmpdic:
                tmpdic[s] -= 1
                if tmpdic[s] == 0:
                    count -= 1
        if count == 0:  # means we have found all the characters
            # find the shortest word
            if minlens > len(i):
                ans = i
                minlens = len(i)
    return ans


print shortestCompletingWord('stsp', ['step', 'steps', 'pest'])



