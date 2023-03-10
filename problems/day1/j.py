def check_sides(i,j,matrix):
    top = min(matrix[i+1][j],matrix[i][j+1])
    bot = max(matrix[i-1][j],matrix[i][j-1])
    if top-bot==1:
        return matrix, 1
    matrix[i][j]=top-1
    return matrix, 0


def BIGBOI():
    n,m = map(int, input().split()) 
    matrix = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n-1):
        if(matrix[i][0]>=matrix[i+1][0] or matrix[i][m-1]>=matrix[i+1][m-1]):
            print(-1)
            return matrix, 0
    for i in range(m-1):
        if(matrix[0][i]>=matrix[0][i+1] or matrix[n-1][i]>=matrix[n-1][i+1]):
            print(-1)
            return matrix, 0
    for i in range(n-2,0,-1):
        for j in range(m-2,0,-1):
            if(matrix[i][j]==0):
                matrix, ret = check_sides(i, j, matrix)
                if ret:
                    print(-1)
                    return matrix, 0
            elif(matrix[i][j]>=matrix[i+1][j] or matrix[i][j]>=matrix[i][j+1] or matrix[i][j]<=matrix[i-1][j] or matrix[i][j]<=matrix[i][j-1]):
                print(-1)
                return matrix, 0
    return matrix, 1

mat, ret = BIGBOI()
if ret:
    print(sum(sum(mat,[])))