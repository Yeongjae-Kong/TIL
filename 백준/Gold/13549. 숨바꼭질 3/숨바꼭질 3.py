from collections import deque

def bfs(n, k):
    if n >= k:
        return n - k
    
    visited = [False] * 100001
    queue = deque([(n, 0)])  # (위치, 시간) 형태로 큐에 저장
    visited[n] = True

    while queue:
        x, time = queue.popleft()
        if x == k:
            return time

        # 순간이동하는 경우
        nx = x * 2
        if 0 <= nx <= 100000 and not visited[nx]:
            queue.appendleft((nx, time))  # 순간이동을 먼저 고려
            visited[nx] = True

        # 걷는 경우
        for nx in (x - 1, x + 1):
            if 0 <= nx <= 100000 and not visited[nx]:
                queue.append((nx, time + 1))
                visited[nx] = True

# 입력 받기
n, k = map(int, input().split())

# BFS 함수 호출 후 결과 출력
result = bfs(n, k)
print(result)