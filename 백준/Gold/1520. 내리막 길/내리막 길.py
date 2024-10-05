import sys
sys.setrecursionlimit(10**9)

m, n = map(int, input().split())

lst = []
for i in range(m):
    lst.append(list(map(int, input().split())))

d = [(0,1),(1,0),(0,-1),(-1,0)]

dp = [[-1]*n for i in range(m)]
def dfs(x,y):
    if x==n-1 and y==m-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and lst[y][x] > lst[ny][nx]:
            dp[y][x] += dfs(nx, ny)
    return dp[y][x]
dfs(0,0)
print(dp[0][0])