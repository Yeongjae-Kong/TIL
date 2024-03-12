def bfs(r,c):
    global ans
    for d in range(4): # 4방향 탐색
        nr = r + dir[d][0]
        nc = c + dir[d][1]
        
        # 경계선 검사
        if 0 <= nr < R and 0 <= nc < C:
        
        	# 바로 근처가 양인 경우 ans는 0
            if farm[nr][nc] == 'S':
                ans = 0
                return
                
            # 아닌 경우 주변을 모두 울타리로
            elif farm[nr][nc] == '.' or farm[nr][nc] == 'D':
                farm[nr][nc] = 'D'

# 데이터 입력받기
R, C = map(int, input().split())
farm = [list(input()) for _ in range(R)]
dir = [[-1,0],[0,1],[1,0],[0,-1]] # 4방탐색
ans = 1

for i in range(R):
    for j in range(C):
    	# 늑대가 위치한 좌표를 탐색 후 해당 좌표로 함수 실행
        if farm[i][j] == 'W':
            bfs(i,j)
            if ans == 0: # ans가 0인 경우에는 이중반복문 모두 중단
                break
    if ans == 0:
        break

# ans의 값에 따라 출력 데이터 조정
if ans == 0:
    print(ans)
else:
    print(ans)
    for f in farm:
        print(''.join(f))