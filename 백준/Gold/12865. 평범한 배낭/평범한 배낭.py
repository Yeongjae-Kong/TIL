import sys

N, K = map(int, input().split())
lst = [[0,0]]
bag = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    lst.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = lst[i][0] 
        value = lst[i][1]
       
        if j < weight:
            bag[i][j] = bag[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            bag[i][j] = max(value + bag[i - 1][j - weight], bag[i - 1][j])

print(bag[N][K])