from itertools import permutations

def is_match(u, b):
    return len(u) == len(b) and all(bc == '*' or uc == bc for uc, bc in zip(u, b))

def solution(user_id, banned_id):
    cases = set()
    for perm in permutations(user_id, len(banned_id)):
        if all(is_match(u, b) for u, b in zip(perm, banned_id)):
            cases.add(frozenset(perm))  # 순서 상관 없으므로 set으로 처리
    return len(cases)
