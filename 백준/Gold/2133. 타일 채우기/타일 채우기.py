n = int(input())

dp = [0] * 30

dp[1] = 3
dp[3] = 11
for i in range(4, n):
    if i%2 == 1: # 6, 8, ..
        dp[i] = dp[i-2]*3 + sum(dp[:i-2])*2 + 2

print(dp[n-1])