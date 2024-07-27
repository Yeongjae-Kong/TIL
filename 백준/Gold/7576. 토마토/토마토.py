from collections import deque

m, n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
q = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] == 0:
                lst[nx][ny] = lst[x][y] + 1
                q.append([nx, ny])

bfs()
for i in lst:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
print(cnt - 1)