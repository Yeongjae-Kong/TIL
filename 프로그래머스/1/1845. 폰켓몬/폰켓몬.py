def solution(nums):
    n = len(nums) // 2
    s = set(nums)
    if len(s) >= n:
        answer = n
    else:
        answer = len(s)
    return answer