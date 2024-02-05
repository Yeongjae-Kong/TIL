# 11048 이동하기

import sys

N, M = map(int, input().split())

lst = []
dp = [[0] * (M + 1)] * (N + 1) # memoization

for i in range(N):
    tmp = list(map(int, input().split()))
    lst.append(tmp)

for i in range(N):
    for j in range(M):
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j]) + lst[i][j]

print(dp[N][M])