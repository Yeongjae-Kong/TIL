# n, m <= 500
# 열을 기준으로 값이 1인 지역들의 좌표를 찾고
# 그 좌표에서 시작한 bfs, 이후 총 길이의 합
# 각 열에 대해 모두 구하고 max
from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    q = deque()
    visited = [[0]*m for _ in range(n)]
    lst = [0]*m

    def bfs(x, y):
        tmp_x = []

        cnt = 0
        q.append((x,y))
        if visited[y][x] == 0:
            visited[y][x] = 1
            cnt += 1
            tmp_x.append(x)
        while q:
            x,y = q.popleft()
            for dx, dy in d:
                nx = x+dx
                ny = y+dy
                if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and land[ny][nx] == 1:
                    visited[ny][nx] = 1
                    cnt+=1
                    tmp_x.append(nx) #x값들 저장 후 cnt만큼 다 더하고 다시 bfs 안돌도록
                    q.append((nx, ny))
        tmp_x = set(tmp_x)

        for i in tmp_x:
            lst[i] += cnt

        return

    for i in range(m): #x
        for j in range(n): #y, 세로 쭉 탐색 이후 가로로 한칸 이동
            if land[j][i] == 1 and not visited[j][i]:
                bfs(i, j)
    
    answer = max(lst)

    return answer