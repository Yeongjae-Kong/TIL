n = int(input())
lst = []
for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        lst.pop()
    else:
        lst.append(tmp)
print(sum(lst))
 