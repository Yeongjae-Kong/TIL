from collections import deque

n, m = map(int, input().split())

lst = []

for _ in range(n):
    lst.append(list(map(int, input())))

q = deque()

d = [(0,1),(1,0),(0,-1),(-1,0)]
visited=[[0]*m for i in range(n)]

def bfs():
    q.append((0,0))
    visited[0][0] = 1
    tmp = 0
    while q:
        x,y = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and lst[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x]+1
                q.append((nx,ny))
    ans = visited[n-1][m-1]
                
    return ans
    
print(bfs())