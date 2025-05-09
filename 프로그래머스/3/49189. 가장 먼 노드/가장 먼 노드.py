from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    q=deque()
    visited = [0]*(n+1)
    distance = [0]*(n+1)
    q.append(1) # node,
    while q:
        node = q.popleft()
        visited[node] = 1
        for n in graph[node]:
            if not visited[n]:
                visited[n] = 1
                distance[n] = distance[node]+1
                q.append((n))
    return distance.count(max(distance[1:]))





# import heapq

# def solution(n, edge):
#     answer = 0
#     graph = [[]*(n+1) for _ in range(n+1)]
#     for i,j in edge:
#         graph[i].append((j, 1))
#         graph[j].append((i, 1))
#     distance = [100000]*(n+1)
#     distance[1] = 0
#     heap = [(0, 1)] # 간선 개수, 시작 노드
#     while heap:
#         cnt, node = heapq.heappop(heap)
#         if cnt > distance[node]:
#             continue
#         for n, cost in graph[node]:
#             new_cost = cnt+cost
#             if new_cost < distance[n]:
#                 distance[n] = new_cost
#                 heapq.heappush(heap, (new_cost, n))

#     max_n = max(distance[1:])
#     answer = distance.count(max_n)
#     return answer