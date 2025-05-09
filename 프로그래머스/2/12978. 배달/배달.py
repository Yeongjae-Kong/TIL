import heapq

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    distance = [500001]*(N+1)
    distance[1] = 0 # 1번 마을에서 시작
    heap = [(0, 1)] # 비용, 현재 마을
    
    while heap:
        cost1, now = heapq.heappop(heap)
        if distance[now] < cost1:
            continue # 이미 최소이므로 다음 루프로
        for dest, cost in graph[now]:
            n_cost = cost1+cost
            if n_cost < distance[dest]:
                distance[dest] = n_cost
                heapq.heappush(heap, (n_cost, dest))
    answer = len([distance[i] for i in range(1, len(distance)) if distance[i] <= K] )
    
    
    return answer