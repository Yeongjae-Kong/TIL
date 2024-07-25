from collections import deque

n = int(input())
lst = [0] * n
for i in range(n):
    lst[i] = list(map(int, input().strip()))
    
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    lst[x][y] = 0
    count = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and lst[nx][ny] == 1:
                q.append((nx, ny))
                lst[nx][ny] = 0
                count += 1
    return count

ans = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            tmp = bfs(i, j)
            ans.append(tmp)
ans.sort()

print(len(ans))
for i in range(len(ans)):
    print(ans[i])