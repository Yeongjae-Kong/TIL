# 11048 이동하기

import sys

N, M = map(int, input().split())

lst = []
dp = [[0] * (M + 1)] * (N + 1)

for i in range(N):
    tmp = list(map(int, input().split()))
    lst.append(tmp)

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + lst[i-1][j-1]
        
print(dp[N][M])