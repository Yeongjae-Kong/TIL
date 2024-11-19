def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [[0]*i for i in range(1, n+1)]
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[1][0]
    dp[1][1] = triangle[1][1]
    for i in range(1, n):
        for j in range(i):
            dp[i][j] = max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j])
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
    answer = max(dp[n-1])
        
    return answer