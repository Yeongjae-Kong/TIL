import sys
from collections import deque
sys.setrecursionlimit(10**9)

n, m, v = map(int, input().split())
lst = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    lst[a][b] = 1
    lst[b][a] = 1

visited1 = [0]*(n+1)
visited2 = [0]*(n+1)

ans = []
def dfs(v):
    visited1[v] = 1
    ans.append(v)
    for i in range(1, len(lst)):
        if lst[v][i] == 1 and not visited1[i]:
            dfs(i)
    return ans

q = deque()
ans2 = []
def bfs(v):
    q.append(v)
    ans2.append(v)
    visited2[v] = 1
    while q:
        tmp = q.popleft()
        for i in range(1, len(lst[tmp])):
            if lst[tmp][i] == 1 and not visited2[i]:
                q.append(i)
                ans2.append(i)
                visited2[i] = 1
    return ans2
print(*dfs(v))
print(*bfs(v))
