from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])  # (현재 인덱스, 현재 합)
    count = 0
    
    while queue:
        index, total = queue.popleft()
        
        if index == len(numbers):  # 모든 숫자를 처리한 경우
            if total == target:
                count += 1
        else:
            queue.append((index + 1, total + numbers[index]))  # 더하는 경우
            queue.append((index + 1, total - numbers[index]))  # 빼는 경우
    
    return count