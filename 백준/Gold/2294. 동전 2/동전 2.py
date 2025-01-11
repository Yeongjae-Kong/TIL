n, k = map(int, input().split())

lst = []

for _ in range(n):
    lst.append(int(input()))

# lst [1, 5, 12]

# dp = cnt 수

dp = [100001]*(k+1)

for i in range(k+1):
    if i in lst:
        dp[i] = 1

for i in range(1, k+1):
    for j in lst:
        if i+j <= k:
            dp[i+j] = min(dp[i]+1, dp[i+j])

if dp[k] > 100000:
    print(-1)
else:
    print(dp[k])