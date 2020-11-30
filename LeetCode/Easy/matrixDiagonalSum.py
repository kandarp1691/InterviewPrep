def matrixDiagonalSum(mat):
    map = {}
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            if i==j or i+j==len(mat)-1:
                map[(i,j)] = mat[i][j]
    sum = 0
    for k,v in map.iteritems():
        sum = sum + v
    return sum
mat = [[1,2,3], [4,5,6], [7,8,9]]
print matrixDiagonalSum(mat)