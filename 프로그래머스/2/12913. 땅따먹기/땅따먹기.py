def solution(land):
    answer = 0
    n = len(land)
    dp = [[0]*4 for _ in range(n)]
    dp[0] = land[0]
    for i in range(1, n):
        for j in range(3):
            dp[i][j] = land[i][j] + max(dp[i-1][:j]+dp[i-1][j+1:])
        dp[i][3] = land[i][3]+max(dp[i-1][:3])
    answer = max(dp[-1])
    return answer