n = int(input())

lst = list(map(int, input().split()))
num = int(input())
for _ in range(num):
    a, t = map(int, input().split())
    t-=1
    if a == 1: # men
        for i in range(t, n, t+1):
            lst[i] = 1-lst[i]
    if a == 2:
        i=1
        lst[t] = 1-lst[t]
        while 0<=t-i<n and 0<=t+i<n:
            if lst[t-i] == lst[t+i]:
                lst[t-i] = 1-lst[t-i]
                lst[t+i] = 1-lst[t+i]
                i+=1
            else:
                break

for i in range(0, n, 20):
    tmplst = lst[i:i+20]
    print(*tmplst)