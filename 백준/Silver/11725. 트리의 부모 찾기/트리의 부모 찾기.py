import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, (input().split()))
    graph[a].append(b)
    graph[b].append(a)

parent = [0]*(n+1)

def dfs(n):
    for i in graph[n]:
        if parent[i] == 0:
            parent[i] = n
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(parent[i])