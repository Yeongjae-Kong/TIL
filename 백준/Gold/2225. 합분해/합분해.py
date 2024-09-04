import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0]*n for _ in range(k)]

for j in range(n):
    dp[0][j] = 1
    if k>1:
        dp[1][j] = j+2
for i in range(k):
    dp[i][0] = i+1
    
for i in range(2, k):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]

print(dp[k-1][n-1]%1000000000)

