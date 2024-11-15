from collections import deque

n = int(input())  # 컴퓨터 수
m = int(input())  # 네트워크 상에서 직접 연결된 쌍의 수

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

# 그래프 입력 받기
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 양방향 연결

# BFS 함수
def bfs(start):
    q = deque([start])
    visited[start] = 1  # 시작 노드 방문 표시
    count = 0

    while q:
        tmp = q.popleft()
        for i in graph[tmp]:
            if not visited[i]:  # 방문하지 않은 노드만 탐색
                visited[i] = 1
                q.append(i)
                count += 1  # 감염된 컴퓨터 수 증가

    return count

# 1번 컴퓨터로부터 시작
result = bfs(1)
print(result)