n, m = map(int, input().split())
lst = [i+1 for i in range(n)]
tmp = []
for i in range(m):
    a, b = map(int, input().split())
    lst[a-1], lst[b-1] = lst[b-1], lst[a-1]
print(*lst)


