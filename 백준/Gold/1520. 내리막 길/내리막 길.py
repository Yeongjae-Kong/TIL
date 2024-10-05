import sys
sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 이동 방향: 동, 남, 서, 북
dp = [[-1]*m for _ in range(n)]
def dfs(x, y):
    if x==m-1 and y==n-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0 <= nx < m and 0 <= ny < n and lst[y][x] > lst[ny][nx]:
            dp[y][x] += dfs(nx, ny)
    return dp[y][x]
print(dfs(0,0))