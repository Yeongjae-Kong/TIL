def solution(a, b):
    if a > b:
        tmp = a
        a = b
        b = tmp
    answer = 0
    for i in range(a, b+1):
        answer += i
    return answer