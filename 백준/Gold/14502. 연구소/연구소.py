# 2의 좌표 받고
# 거기에서 if 0이면 q에넣고 bfs

from collections import deque
import copy
from itertools import combinations

n, m = map(int, input().split())

lst = []
d = [(0,1), (1,0), (-1,0), (0,-1)]

def bfs(lst):
    q = deque()
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m and lst[nx][ny] == 0:
                lst[nx][ny]=2
                q.append((nx, ny))

for i in range(n):
    lst.append(list(map(int, input().split())))

dp = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            dp.append((i,j))
            
ans = 0
for c in combinations(dp, 3):
    cnt = 0
    tmplst = copy.deepcopy(lst)
    for x, y in c:
        tmplst[x][y] = 1
    bfs(tmplst)
    for i in range(n):
        cnt += tmplst[i].count(0)
    if cnt > ans:
        ans = cnt
print(ans)