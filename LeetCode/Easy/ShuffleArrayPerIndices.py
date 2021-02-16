def shuffleasperindices(s, indices):
    ans = [None] * len(indices)
    for i in range(0, len(indices)):
        ans[indices[i]] = s[i]
    return "".join(ans)
str = 'codeleet'
indices = [4,5,6,7,0,2,1,3]
print shuffleasperindices(str, indices)