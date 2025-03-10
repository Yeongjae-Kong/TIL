from itertools import combinations

def solution(nums):
    temp = []
    for a, b, c in combinations(nums, 3):
        temp.append(a+b+c)
    cnt = len(temp)
    for i in temp:
        for j in range(2, i):
            if i % j == 0:
                cnt -= 1
                break

    return cnt