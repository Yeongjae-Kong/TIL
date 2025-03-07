import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        return cnt
    while len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville) * 2
        heapq.heappush(scoville, a+b)
        cnt += 1
        if scoville[0] >= K:
            return cnt
    
    return -1