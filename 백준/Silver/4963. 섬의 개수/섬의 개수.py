from collections import deque

ans = []

def bfs(i, j):
    q = deque()
    q.append((i,j))
    while q:
        a,b = q.popleft()
        for dx, dy in d:
            nx = b+dx
            ny = a+dy
            if 0<=ny<y and 0<=nx<x and lst[ny][nx]==1:
                lst[ny][nx] = 0
                q.append((ny, nx))

d = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

while True:
    x,y = map(int, input().split())
    if x==0 and y==0:
        break
    else:
        cnt=0
        lst = []
        for _ in range(y):
            lst.append(list(map(int,input().split())))
        for i in range(y):
            for j in range(x):
                if lst[i][j] == 1:
                    bfs(i, j)
                    cnt+=1
        ans.append(cnt)

for i in range(len(ans)):
    print(ans[i])
