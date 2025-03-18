def solution(n):
    cnt = 0
    n = str(n)
    for i in n:
        cnt += int(i)
    answer = cnt
    return answer