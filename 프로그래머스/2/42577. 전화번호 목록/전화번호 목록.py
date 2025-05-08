from collections import defaultdict

def solution(phone_book):
    answer = True
    dic = defaultdict(int)
    for num in phone_book:
        num_len = len(num)
        for i in range(1, num_len+1):
            dic[num[:i]] += 1
    for num in phone_book:
        if dic[num] >= 2:
            answer = False
            return answer
    return answer