n = int(input())  # 스위치 개수
lst = list(map(int, input().split()))  # 스위치 상태
num = int(input())  # 학생 수

for _ in range(num):
    a, t = map(int, input().split())
    t -= 1  # 0-index로 맞추기
    
    if a == 1:  # 남학생
        for i in range(t, n, t + 1):
            lst[i] = 1 - lst[i]  # 스위치 상태를 반전시킴
    
    if a == 2:  # 여학생
        i = 0
        lst[t] = 1 - lst[t]  # 본인 스위치 상태 반전
        while t - i >= 0 and t + i < n:
            if lst[t - i] == lst[t + i]:  # 대칭 구간 탐색
                lst[t - i] = 1 - lst[t - i]
                lst[t + i] = 1 - lst[t + i]
                i += 1
            else:
                break

# 결과 출력: 20개씩 출력
for i in range(0, n, 20):
    print(*lst[i:i+20])
