import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [0] * n

for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp)+1)