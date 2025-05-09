import heapq

def solution(n, edge):
    answer = 0
    graph = [[]*(n+1) for _ in range(n+1)]
    for i,j in edge:
        graph[i].append((j, 1))
        graph[j].append((i, 1))
    distance = [100000]*(n+1)
    distance[1] = 0
    heap = [(0, 1)] # 간선 개수, 시작 노드
    while heap:
        cnt, node = heapq.heappop(heap)
        if cnt > distance[node]:
            continue
        for n, cost in graph[node]:
            new_cost = cnt+cost
            if new_cost < distance[n]:
                distance[n] = new_cost
                heapq.heappush(heap, (new_cost, n))

    max_n = max(distance[1:])
    answer = distance.count(max_n)
    return answer