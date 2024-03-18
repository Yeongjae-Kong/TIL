from collections import deque

def bfs(n, m, arr):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque([(0, 0, 0)])  # (x, y, 벽 부순 횟수)
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1

    while queue:
        x, y, broken = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][broken]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    queue.append((nx, ny, broken))
                elif broken == 0 and arr[nx][ny] == 1 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))

    return -1

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

print(bfs(n, m, arr))