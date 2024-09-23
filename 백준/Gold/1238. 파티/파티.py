# 다익스트라 - 특정 벌텍스에서 나머지 모든 벌텍스로 가는 최단 비용
# 위 문제는 N명이 특정 벌텍스로 가는 데 걸리는 비용.
# 따라서 그래프의 방향을 바꿔 특정 벌텍스에서 N명에게 가는 비용을 구하면 편함.


import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
reversed_graph = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((t,e))
    reversed_graph[e].append((t,s))

def dijkstra(graph, start):
    distance = [INF]*(N+1)
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        now_cost, now_node = heapq.heappop(heap)
        if distance[now_node] < now_cost:
            continue
        for tmp_cost, tmp_node in graph[now_node]:
            cost = distance[now_node] + tmp_cost
            if cost < distance[tmp_node]:
                distance[tmp_node] = cost
                heapq.heappush(heap, (cost, tmp_node))
    return distance

# 마을 X -> 각 마을
come = dijkstra(graph,X)
# 각 마을 -> 마을 X
go = dijkstra(reversed_graph,X)

max_dist = 0
for i in range(1, N+1):
    total_dist = go[i] + come[i]
    max_dist = max(max_dist, total_dist)

print(max_dist)