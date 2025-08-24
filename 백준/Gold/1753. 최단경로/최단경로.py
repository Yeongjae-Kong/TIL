import heapq
import math
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
dist = [math.inf]*(V+1)
dist[k] = 0
q = [(0, k)] # w, k 초기화

while q:
    w, k = heapq.heappop(q) 
    if dist[k] > w: # 이미 더 짧은 거리로 업데이트됐으면 패스
        continue
    for nextv, nextw in graph[k]: # k에서 갈 수 있는 간선 체크
        if w+nextw < dist[nextv]:
            dist[nextv] = w+nextw
            heapq.heappush(q, (w+nextw, nextv))
            
for i in range(1, len(dist)):
    if (dist[i] == math.inf):
        print("INF")
    else:
        print(dist[i])