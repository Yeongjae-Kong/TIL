from collections import deque

N = int(input())
a = [list(input()) for _ in range(N)]
q = deque()

# 색약 x
visited = [[0] * N for _ in range(N)]
cnt1 = 0
d = [(0,1), (1,0), (0,-1), (-1,0)]

def BFS(x,y):
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우
            if 0<=nx<N and 0<=ny<N and a[nx][ny] == a[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문체크 후 큐에 append
                q.append((nx,ny))
                
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
            cnt1 += 1

# 색약 o
for i in range(N):
    for j in range(N):
        if a[i][j] == 'G':
            a[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
            cnt2 += 1

print(cnt1, cnt2)