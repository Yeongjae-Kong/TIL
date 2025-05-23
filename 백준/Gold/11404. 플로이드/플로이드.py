import sys
INF = int(1e9)

n = int(sys.stdin.readline())  # 도시의 수
m = int(sys.stdin.readline())  # 버스의 수

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] =  0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, len(graph)):
    for j in range(1, len(graph[i])):
        if graph[i][j] == INF:
            graph[i][j] = 0
        print(graph[i][j], end=' ')
    print(end='\n')
        