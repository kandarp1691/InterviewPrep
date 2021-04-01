def partitionLabels(S):
    lastOcc = [None] * 26
    for i in range(0, len(S)):
        lastOcc[ord(S[i]) - ord('a')] = i
    ans = []
    anchor = 0
    j = 0
    for i in range(0, len(S)):
        j = max(j, lastOcc[ord(S[i]) - ord('a')])
        if i == j :
            ans.append(i - anchor + 1)
            anchor = i + 1
    return ans

S = 'ababcbacadefegdehijhklij'
print partitionLabels(S)

        


