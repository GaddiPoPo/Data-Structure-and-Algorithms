def solution(matrix,visited,n,x,y,ans,path):
    # to see the case if rat goes out of a matrix or it stays behind
    if x>=n or y>=n or x<0 or y<0:
        return
    if matrix[x][y]==0:
        return
        # it checks if there is zero in the current block so it get s returned
    if x==n-1 and y==n-1:
        ans.append(path)
        return
    visited[x][y]=1
    # marking as vsisted
    if y+1<n and not visited[x][y+1]:
        solution(matrix,visited,n,x,y+1,ans,path+'R')
        # see on pen and paper by seeeing x and y in 2 d matrix
    if y-1>-1 and not visited[x][y-1]:
        solution(matrix,visited,n,x,y-1,ans,path+'L')
    if x+1<n and not visited[x+1][y]:
        solution(matrix, visited, n, x+1, y, ans, path+'D')
    if x-1>-1 and not visited[x-1][y]:
        solution(matrix, visited, n, x-1, y, ans, path+'U')
    visited[x][y]=0
    #backtracking comes here by marking again to 0
def findpath(matrix,n):
        # n: size of matrix n*n
        # matrix: matrix of n*n

        # start at 0,0
        # end at n-1, n-1
        # 2d array (n*n) for keeping track of visited nodes:
    visited = [[0] * n for i in range(n)]
    ans = []
    solution(matrix, visited, n, 0, 0, ans, '')
    return ans
matrix = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]
result = findpath(matrix, 4)
print("Paths found:")
for path in result:
    print(path)