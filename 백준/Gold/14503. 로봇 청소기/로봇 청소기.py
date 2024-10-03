from collections import deque

N, M = map(int, input().split())

r, c, dir = map(int, input().split())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
d = [(0, -1), (1,0), (0,1),(-1,0)] #x, y

while True:
    i = dir
    breakflag = 0
    cnt = 0
    #현재 칸 청소
    if lst[r][c] == 0:
        lst[r][c] = -1
    n=4
    while n>0: # 4방향
        if i>=1:
            i-=1
        else:
            i=3
        nx = c+d[i][0]
        ny = r+d[i][1]
        # 청소 안한 방
        if lst[ny][nx] == 0:
            c=nx
            r=ny
            dir = i
            break
        else: #방이 청소됐으면 1디렉션 변경 2 네방향 다 봤으면 후진, 디렉션은 그대로
            n-=1
            if n==0:
                if i>=2:
                    i-=2
                elif i<2:
                    i+=2 # 후진 dir
                   
                nx = c+d[i][0]
                ny = r+d[i][1]

                if lst[ny][nx] == 1: #뒤쪽 칸이 벽이면
                    breakflag = 1
                    break
                else: # 후진 가능
                    c = nx
                    r = ny
                    if i>= 2:
                        i-=2
                    elif i<2:
                        i+=2 # 디렉션 유지
                    dir = i
    if breakflag == 1:
        break
        
cnt = 0
for i in range(N):
    cnt += lst[i].count(-1)
print(cnt)