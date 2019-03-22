def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """
    vowel = 'aeiouAEIOU'
    ans = []
    arr = S.split(" ")
    for word in range(0, len(arr)):
        if arr[word][0] in vowel:
            arr[word] = arr[word] + 'ma'
        else:
            arr[word] = arr[word][1:] + arr[word][0] + 'ma'
        acount = ''.join(['a']*(word+1))
        arr[word] = arr[word] + acount
        ans.append(arr[word])

    return ' '.join(ans)

print toGoatLatin('I speak Goat Latin')