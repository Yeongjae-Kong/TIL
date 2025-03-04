from collections import deque

def solution(n, computers):
    visited = [0]*(n)
    answer = 0
    q = deque()
    def bfs(i):
        q.append(i)
        visited[i] = 1
        while q:
            i = q.popleft()
            for j in range(n):
                if computers[i][j] * j != 0: # 연결되있으면 (=1)            
                    if not visited[computers[i][j]*j]: # 그 중 방문안했으면
                        q.append(computers[i][j]*j)
                        visited[computers[i][j]*j] = 1
                    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer