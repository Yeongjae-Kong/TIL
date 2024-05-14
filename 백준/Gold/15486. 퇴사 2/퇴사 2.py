import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
day = []
cost = []
dp = [0]*(n+1)
for i in range(n):
    a, b = map(int, input().split())
    day.append(a)
    cost.append(b)
for i in range(n):
    dp[i] = max(dp[i-1], dp[i])
    if i+day[i] <= n:
        dp[i+day[i]] = max(dp[i+day[i]], dp[i]+cost[i])
print(max(dp))