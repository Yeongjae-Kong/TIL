N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)

result = []

def dfs(start, end, cnt):
    if start == end:
        return cnt
    visited[start] = 1

    for i in graph[start]:
        if not visited[i]:
            temp = dfs(i, end, cnt+1)
            if temp != -1: # start == end를 만족한 경우
                return temp
    return -1
        
print(dfs(A, B, 0))