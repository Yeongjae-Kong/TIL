n = int(input())
lst = []
for _ in range(n):
    lst.append(list(input()))
ans = 0
for i in range(n):
    cnt = 0
    check = set()
    for j in range(len(lst[i])):
        if lst[i][j] not in check:
            cnt+=1
        elif lst[i][j-1] == lst[i][j]:
            cnt+=1
        check.add(lst[i][j])
    if cnt == len(lst[i]):
        ans += 1
        
print(ans)