def commonChild(s1,s2):
    max_length_so_far = 0
    n = len(s1)+1
    m = len(s2)+1

    common_part = [[0]*(n)for i in range(m)]
    for i in range(1, n):
        for j in range(1,m):
            if s1[i-1] == s2[i-1]:
                common_part[i][j] = common_part[i-1][j-1] + 1
            else:
                common_part[i][j] = max(common_part[i-1][j], common_part[i][j-1])

            max_length_so_far = max(common_part[i][j], max_length_so_far)
    return max_length_so_far


print commonChild('NOHARAAA','SHINCHAN')