import sys
input = sys.stdin.readline

num_points = int(input())
avenue = input().rstrip()

dp = [float('inf')] * num_points
dp[0] = 0

for i in range(1, num_points):
    for j in range(i):
        if avenue[j] == 'B' and avenue[i] == 'O':
            dp[i] = min(dp[i], dp[j] + pow(i - j, 2))
        elif avenue[j] == 'O' and avenue[i] == 'J':
            dp[i] = min(dp[i], dp[j] + pow(i - j, 2))
        elif avenue[j] == 'J' and avenue[i] == 'B':
            dp[i] = min(dp[i], dp[j] + pow(i - j, 2))

if dp[num_points - 1] != float('inf'):
    print(dp[num_points - 1])
else:
    print(-1)