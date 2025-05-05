from collections import deque

def solution(storage, requests):
    answer = 0
    # 0 으로 패딩한 다음에
    # 알파벳 하나일 땐 0에 인접하면 접근 가능
    # 알파벳 두개일 땐 전부 접근 가능
    # 
    n, m = len(storage[0]), len(storage) # n = 가로, m = 세로
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    visited = [[0]*(n+2) for _ in range(m+2)] # visited check
    
    lst = [[0]*(n+2) for _ in range(m+2)] # zero padding 추가한 리스트
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            lst[i+1][j+1] = storage[i][j]

    q = deque()
    
    def bfs_1(req):
        visited = [[0]*(n+2) for _ in range(m+2)] # visited check
        q.append((0,0))
        visited[0][0] = 1
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if 0<=nx<n+2 and 0<=ny<m+2 and lst[ny][nx] == 0 and not visited[ny][nx]:
                    q.append((nx, ny))
                    visited[ny][nx] = 1
                elif 0<=nx<n+2 and 0<=ny<m+2 and lst[ny][nx] == req and not visited[ny][nx]:
                    lst[ny][nx] = 0
                    print('bfs 1, ny nx = ', ny, nx, req)
                    visited[ny][nx] = 1
                    
    def bfs_2(req):
        for i in range(m+2):
            for j in range(n+2):
                if lst[i][j] == req:
                    lst[i][j] = 0
                    print('bfs 2')

    for req in requests:
        if len(req) == 1:
            bfs_1(req)
        else:
            bfs_2(req[0])
    
    for sub_lst in lst:
        answer += sub_lst.count(0)
        
    answer = (n+2)*(m+2) - answer
    return answer

# H A H
# H B H
# H H H
# H A H
# H B H