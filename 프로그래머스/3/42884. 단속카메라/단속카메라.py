def solution(routes):
    routes.sort(key=lambda x:x[1])
    print(routes)
    ans = 1
    j = 0
    for i in range(len(routes)-1):
        if routes[j][1] < routes[i+1][0]:
            ans += 1
            j = i+1
    
    return ans
