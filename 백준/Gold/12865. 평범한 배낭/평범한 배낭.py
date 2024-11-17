n, k = map(int, input().split())
weight = []
value = []
for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)
    
dp = [[0]*(k+1) for i in range(n+1)]

# i - item, j - weight, dp = value
# dp[i][j] : i번째까지 item에 대해 무게 j까지 최댓값
#   1 2 3 4 5 6 7
# 1           13 13
# 2       8 8 13 13
# 3     6 8 8 13 14
# 4

for i in range(1,n+1):
    for j in range(1,k+1):
        if weight[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]]+value[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])