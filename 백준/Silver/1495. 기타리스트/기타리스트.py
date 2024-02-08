n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True

for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[i - 1][j]:
            if j + volumes[i - 1] <= m:
                dp[i][j + volumes[i - 1]] = True
            if j - volumes[i - 1] >= 0:
                dp[i][j - volumes[i - 1]] = True

max_volume = -1
for volume in range(m, -1, -1):
    if dp[n][volume]:
        max_volume = volume
        break

print(max_volume)