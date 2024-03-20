from collections import deque

def bfs():
    q = deque()
    visited = set()
    parent = {}  # 각 노드의 이전 노드를 저장할 딕셔너리
    
    a, b = map(int, input().split())
    q.append(a)
    visited.add(a)
    
    while q:
        tmp = q.popleft()
        
        if tmp == b:
            path = []
            curr = b
            while curr != None:
                path.append(curr)
                curr = parent.get(curr, None)  # 이전 노드로 이동
            path.reverse()
            print(len(path) - 1)  # 시작 노드는 제외
            print(' '.join(map(str, path)))
            return
        
        for i in [tmp - 1, tmp + 1, tmp * 2]:
            if 0 <= i <= 100000 and i not in visited:
                q.append(i)
                visited.add(i)
                parent[i] = tmp  # i의 이전 노드는 tmp

bfs()