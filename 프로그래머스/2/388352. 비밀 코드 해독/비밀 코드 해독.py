from itertools import combinations

def solution(n, q, ans):
    candidates = list(combinations(range(1, n+1), 5))  # 가능한 5개 조합
    result = 0

    for comb in candidates:
        valid = True
        code_set = set(comb)

        for i in range(len(q)):
            match = sum(1 for num in q[i] if num in code_set)
            if match != ans[i]:
                valid = False
                break

        if valid:
            result += 1

    return result
