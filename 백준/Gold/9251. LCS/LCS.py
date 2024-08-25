# dp에 최대 부분수열 길이 저장
# 같은 알파벳이 있으면 수열길이+1을 해주는데, 이전에 나왔던 길이 고려해야함.

# A C A Y K P
# C A P C A K
#[0 1 0 0 1 0] loop 1
#[1 1 0 2 1 0] loop 2 
#[1 2 0 2 3 0] loop 3 ...

# 같은게 있으면 count += 1 
# 단, 누적했던 부분 수열 길이(=count)보다 클 때 업데이트해야함. 같거나 작으면 상관없으므로, count를 dp[j]로.

import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()
dp = [0] * len(word2)

for i in range(len(word1)): # ACAYKP
    cnt = 0
    for j in range(len(word2)): # C A P C A K
        if cnt < dp[j]: # 누적값 업데이트
            cnt = dp[j]
        elif word1[i] == word2[j]:
            dp[j] = cnt + 1
print(max(dp))