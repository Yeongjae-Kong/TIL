def solution(s):
    answer = False
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(s) == 4 or len(s) == 6:
        answer = True
    for i in s:
        if i in alpha:
            answer = False
    return answer