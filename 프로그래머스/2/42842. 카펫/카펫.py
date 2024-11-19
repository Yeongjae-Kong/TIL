def solution(brown, yellow):
    for i in range(brown):
        if (brown+yellow) / (((brown+4) / 2 )- i) == i:
            ans = i
            break
    answer = [ans, (brown+yellow)/ans]
    answer.sort(reverse=True)
    return answer