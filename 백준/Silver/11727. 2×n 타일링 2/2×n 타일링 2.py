
# n = 1 -> 1
# n = 2 -> 3
# n = 3 -> 5
# n = 4 -> 9

n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1]+2*dp[i-2]

print(dp[n] % 10007)