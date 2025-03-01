from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  # 맵의 크기
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 이동 방향 (남, 북, 동, 서)

    queue = deque([(0, 0, 1)])  
    while queue:
        x, y, dist = queue.popleft()
        
        if x == n-1 and y == m-1:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny, dist + 1))
                maps[nx][ny] = 0  # 방문 처리(다시 방문하지 않도록)

    return -1