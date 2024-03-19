from collections import deque

def bfs():
    q = deque()
    visited = {}
    a, b = map(int, input().split())
    q.append((a, 0))
    visited[a] = 0

    while q:
        tmp, count = q.popleft()
        if tmp == b:
            return count
        for next_tmp in [tmp - 1, tmp * 2, tmp + 1]:
            if 0 <= next_tmp <= 100000 and (next_tmp not in visited or visited[next_tmp] > count + 1):
                q.append((next_tmp, count + 1))
                visited[next_tmp] = count + 1

print(bfs())