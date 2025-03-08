def solution(arr):
    n = (len(arr) + 1) // 2 

    dp_max = [[-float('inf')] * n for _ in range(n)]
    dp_min = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = dp_min[i][i] = int(arr[i * 2])

    for length in range(2, n + 1): 
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                op = arr[k * 2 + 1] 

                if op == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j])
                else:  # '-'
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j])

    return dp_max[0][n-1]
