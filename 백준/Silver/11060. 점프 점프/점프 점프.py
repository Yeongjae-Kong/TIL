n = int(input())
arr = list(map(int, input().split()))

dp = [1001]*(n)
dp[0]=0

for i in range(n):
    for j in range(1, arr[i]+1):
        if i+j < n:
            dp[i+j] = min(dp[i+j], dp[i]+1)
if dp[n-1] == 1001:
    print(-1)
else:
    print(dp[n-1])