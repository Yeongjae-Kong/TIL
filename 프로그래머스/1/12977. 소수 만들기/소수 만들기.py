from itertools import combinations
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # √n까지만 확인
        if n % i == 0:
            return False
    return True

def solution(nums):
    prime_count = 0
    for a, b, c in combinations(nums, 3):
        if is_prime(a + b + c):
            prime_count += 1
    return prime_count
