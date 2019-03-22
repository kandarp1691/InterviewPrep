def designer_pdf(word):
    max_height = 0
    result_list = []
    arr = [4, 2, 1, 2, 3, 4, 3, 7, 4, 1, 5, 6, 1, 3, 2, 6, 6, 3, 7, 3, 1, 1, 5, 1, 1, 4]
    for ch in range(0, len(word)):
        index = ord(word[ch]) - ord('a')
        if arr[index] > max_height:
            max_height = arr[index]
    print max_height*len(word)

designer_pdf('qjhwkcexec')
