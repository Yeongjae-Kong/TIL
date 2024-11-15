# 계단의 개수 입력
n = int(input())

# 각 계단의 점수를 입력받기 위한 리스트
stairs = [0] * (n + 1)
for i in range(1, n + 1):
    stairs[i] = int(input())

# 예외 처리: 계단이 1개 또는 2개인 경우를 바로 처리
if n == 1:
    print(stairs[1])
    exit()
elif n == 2:
    print(stairs[1] + stairs[2])
    exit()

# DP 테이블 초기화
dp = [0] * (n + 1)

# 초기 값 설정
dp[1] = stairs[1]  # 첫 번째 계단 점수
dp[2] = stairs[1] + stairs[2]  # 첫 번째와 두 번째 계단 점수의 합

# DP 점화식 적용
for i in range(3, n + 1):
    # i번째 계단까지의 최댓값을 구할 때 두 가지 경우를 고려
    # 1. (i-2)번째 계단에서 두 계단 올라온 경우
    # 2. (i-3)번째 계단에서 한 계단 올라오고 (i-1)번째 계단을 밟고 올라온 경우
    dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

# 최댓값 출력 (마지막 계단을 밟았을 때)
print(dp[n])
