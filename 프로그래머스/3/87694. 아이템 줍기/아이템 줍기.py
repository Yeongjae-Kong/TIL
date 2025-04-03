from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # dx, dy 기준 
    # while q:
    # if 테두리:
    #    q.append()
    # 사각형은 최대 4개, 그렇다면 테두리를 어떻게 인식하느냐?
    # 새로운 사각형 테두리를 우선 1로 처리한 후, 이전 모든 사각형에 대해 x0< <x1 and y0< <y1 일 때 0으로 바꾸기? << 꺾여지는 코너에서 경로를 표현하지 못함.
    # 따라서 두칸씩 만들고, 카운트할때도 두칸씩 이동 및 계산
    map = [[0]*101 for _ in range(101)] # 나중에 101로 고치기
    
    # 모든 테두리 1
    for i in range(len(rectangle)):
        x0, x1 = rectangle[i][0]*2, rectangle[i][2]*2
        y0, y1 = rectangle[i][1]*2, rectangle[i][3]*2
        for j in range(x0, x1+1):
            map[y0][j] = 1
            map[y1][j] = 1
        for j in range(y0, y1+1):
            map[j][x0] = 1
            map[j][x1] = 1
    # 내부는 다시 0으로
    for i in range(len(rectangle)):
        x0, x1 = rectangle[i][0]*2, rectangle[i][2]*2
        y0, y1 = rectangle[i][1]*2, rectangle[i][3]*2
        for j in range(x0+1, x1): #(2~6)
            for k in range(y0+1, y1): #(2~3)
                if map[k][j] == 1:
                    map[k][j] = 0
    # for i in range(len(map)):
    #     print(map[-i])
    
    # bfs
    q = deque()
    q.append((characterX*2, characterY*2, 0))
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    visited = [[0]*101 for _ in range(101)]
    while q:
        x, y, cnt = q.popleft()
        if x==itemX*2 and y==itemY*2:
            cnt = cnt / 2
            return cnt
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0<=nx<=100 and 0<=ny<=100 and map[ny][nx] == 1 and not visited[ny][nx]:
                q.append((nx, ny, cnt+1))
                visited[ny][nx] = 1