n = int(input())

dp = [[0]*10 for i in range(n+1)]

for i in range(1, 10):
    dp[1][i] = 1

for c in range(2, n+1):
    for i in range(10):
        if i == 0:
            dp[c][i] = dp[c-1][i+1]
        elif i == 9:
            dp[c][i] = dp[c-1][i-1]
        else:
            dp[c][i] = dp[c-1][i-1]+dp[c-1][i+1]

print(sum(dp[n])%1000000000)