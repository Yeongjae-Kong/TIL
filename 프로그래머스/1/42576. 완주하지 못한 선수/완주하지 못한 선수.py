def solution(participant, completion):
    dic = {}
    for name in participant:
        if name in dic.keys():
            dic[name] += 1
        else:
            dic[name] = 1
    for name in completion:
        dic[name] -= 1
    answer = [k for k,v in dic.items() if v>0]
    
    return answer[0]