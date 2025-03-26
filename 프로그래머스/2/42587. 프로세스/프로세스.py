from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])  # (index, priority)
    execution_order = 0

    while queue:
        cur = queue.popleft()
        
        # 현재 프로세스보다 높은 우선순위가 남아있는지 확인
        if any(cur[1] < other[1] for other in queue):
            queue.append(cur)
        else:
            execution_order += 1
            if cur[0] == location:
                return execution_order
