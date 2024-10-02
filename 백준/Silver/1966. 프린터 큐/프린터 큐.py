n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt=0
    while len(lst) >= 1:
        if lst[0] == max(lst):
            if b != 0:
                b -= 1
                lst.pop(0)
                cnt+=1
            elif b == 0:
                lst.pop(0)
                cnt+=1
                print(cnt)
                break
        else:
            tmp = lst.pop(0)
            lst.append(tmp)
            if b != 0:
                b -= 1
            elif b == 0:
                b = len(lst)-1