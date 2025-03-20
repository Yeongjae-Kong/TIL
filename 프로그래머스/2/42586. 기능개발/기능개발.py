from collections import deque

def solution(progresses, speeds):
    days = deque()
    for p, s in zip(progresses, speeds):
        remaining_days = -((p - 100) // s)
        days.append(remaining_days)
    
    result = []
    while days:
        count = 1
        deploy_day = days.popleft()
        
        while days and days[0] <= deploy_day:
            count += 1
            days.popleft()
        
        result.append(count)
    
    return result