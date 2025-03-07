def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    ans1, ans2, ans3 = 0, 0, 0
    for i in range(len(answers)):
        a = i % 5
        b = i % 8
        c = i % 10
        if answers[i] == first[a]:
            ans1 += 1
        if answers[i] == second[b]:
            ans2 += 1
        if answers[i] == third[c]:
            ans3 += 1
    temp = []
    answer = []
    temp.append(ans1)
    temp.append(ans2)
    temp.append(ans3)
    max_num = max(temp)
    if temp[0] == max_num:
        answer.append(1)
    if temp[1] == max_num:
        answer.append(2)
    if temp[2] == max_num:
        answer.append(3)
    
    return answer