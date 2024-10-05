#   C A P C A K
# A 0 1 0 0 1 0
# C 1 1 0 2 1 0  C에 대해, 앞에 A=1의 dp가 1이므로 1+1
# A 1 1 0 2 3 0
# Y 1 1 0 2 3 0
# K 1 1 0 2 3 4
# P 1 1 1 2 3 4

a = list(input())
b = list(input())

dp = [0]*len(b)

for i in range(len(a)):
    tmp = 0
    for j in range(len(b)):
        if dp[j] > tmp:
            tmp = dp[j] # 여기서 여태까지의 LCS 저장
        elif a[i] == b[j]:
            dp[j] = tmp+1  # 추가되면 +1
print(max(dp))