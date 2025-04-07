def solution(s):
    setp = "pP"
    sety = "yY"
    checkp = checky = 0
    answer = True
    for i in s:
        if i in setp:
            checkp += 1
        if i in sety:
            checky += 1
    if checkp != checky:
        answer = False

    return answer