from collections import deque

N, M = map(int, input().split())

space = []
for i in range(N):
    tmp = list(map(int, input().split()))
    space.append(tmp)
    
d = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
graph = [[0]*M for i in range(N)]
shark = deque()
for i in range(N): 
    for j in range(M):
        if space[i][j] == 1:
            shark.append([i,j])
            
for i in range(len(shark)):
    x,y=shark[i]
    graph[x][y]=1
    
def bfs():
    while shark:
        x,y=shark.popleft()
        for dx, dy in d:
            x_=x+dx
            y_=y+dy
            if 0 <= x_ <= N-1 and 0 <= y_ <= M-1:
                if graph[x_][y_]==0:
                    shark.append([x_,y_])
                    graph[x_][y_] = graph[x][y]+1
bfs()
print(max(map(max, graph))-1)