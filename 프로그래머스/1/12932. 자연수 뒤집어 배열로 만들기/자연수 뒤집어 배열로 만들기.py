def solution(n):
    
    answer = []
    for i in range(1, len(str(n))+1):
        answer.append(int(str(n)[-i]))
    return answer