
def isSubMatrix(smatrix, bmatrix):
    n= len(smatrix[0])

    for i in range(0, len(bmatrix)-n+1):
        for j in range(0, len(bmatrix[i])-n+1):
            subMat = [[bmatrix[x][y] for y in range(i,i+n)] for x in range(j,j+n)]
            if subMat == smatrix:
                return True
    return False
print isSubMatrix( [[7,7],[10,11]],[[1,2,3,4],[5,6,7,8], [9,10,11,12], [13,14,15,16]])
