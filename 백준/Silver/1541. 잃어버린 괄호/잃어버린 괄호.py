import sys
input = sys.stdin.readline

a = input().split('-')
lst = []
lst.append(a)
ans = []
for i in range(len(lst[0])):
    tmp = lst[0][i]
    sumlst = []
    x = tmp.split('+')
    for i in x:
        sumlst.append(int(i))
    a = sum(sumlst)
    ans.append(a)
t = ans[0]
for i in range(1, len(ans)):
    t -= ans[i]
print(t)
