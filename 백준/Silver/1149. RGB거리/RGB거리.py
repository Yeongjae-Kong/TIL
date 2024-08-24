# 1 10 10
# 1 2 3
# 10 1 10
# > 앞 index만 고려해선 안됨, 뒤도 고려
# 점화식을 구하는게 제일 중요!

import sys
input = sys.stdin.readline

n = int(input())
a = [0]*n

for i in range(n):
    a[i] = list(map(int,input().split()))
    
for i in range(1,n):
    a[i][0]= min(a[i-1][1],a[i-1][2]) + a[i][0]
    a[i][1]= min(a[i-1][0],a[i-1][2]) + a[i][1]
    a[i][2]= min(a[i-1][0],a[i-1][1]) + a[i][2]

print(min(a[n-1][0],a[n-1][1],a[n-1][2]))

