# n개 자연수 중 m개 수열
# 4 2
# 9 7 9 1
from itertools import permutations

n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

ans = []
for c in permutations(lst, m):
    ans.append(c)
    
ans = list(set(ans))
ans.sort()
for i in range(len(ans)):
    print(*ans[i])
