# 12869 뮤탈리스크
# 블로그 참고함

n = int(input())
scv = list(map(int, input().split()))
scv.extend([0, 0])

dp = [[[0]*61 for _ in range(61)] for _ in range(61)]
dp[scv[0]][scv[1]][scv[2]] = 1 
comb = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]
for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0:
                for c in comb:
                    i2 = i-c[0] if i-c[0] >= 0 else 0
                    j2 = j-c[1] if j-c[1] >= 0 else 0
                    k2 = k-c[2] if k-c[2] >= 0 else 0
                    if dp[i2][j2][k2] == 0 or dp[i2][j2][k2] > dp[i][j][k]+1:
                        dp[i2][j2][k2] = dp[i][j][k]+1

print(dp[0][0][0]-1)