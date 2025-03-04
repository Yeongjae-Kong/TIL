from collections import deque

n = int(input())

lst=[]

for _ in range(n):
    lst.append(list(map(int, input())))

q = deque()
visited = [[0]*n for _ in range(n)]
d = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(y,x):
    num = 1 
    q.append((y,x))
    visited[y][x] = 1
    while q:
        y,x = q.popleft()
        for dx, dy in d:
            ny, nx = y+dy, x+dx
            if 0<=ny<n and 0<=nx<n and lst[ny][nx] == 1 and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = 1
                num+=1
    return num
cnt = 0
num_house = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1 and not visited[i][j]:
            temp = bfs(i,j)
            num_house.append(temp)
            cnt+=1
            
num_house.sort()

print(cnt)
for num in num_house:
    print(num)