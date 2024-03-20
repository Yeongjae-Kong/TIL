from collections import deque

def bfs():
    q = []
    visited = {}
    
    a, b = map(int, input().split())
    q.append(a)
    visited[a] = (0, None)  # (count, prev)
    
    while q:
        tmp = q.pop(0)
        count, prev = visited[tmp]
        
        if tmp == b:
            path = []
            while tmp != None:
                path.append(tmp)
                tmp = visited[tmp][1]
            path.reverse()
            print(count)
            print(' '.join(map(str, path)))
            return
        
        for i in [tmp - 1, tmp * 2, tmp + 1]:
            if 0 <= i <= 100000 and i not in visited:
                q.append(i)
                visited[i] = (count + 1, tmp)

bfs()