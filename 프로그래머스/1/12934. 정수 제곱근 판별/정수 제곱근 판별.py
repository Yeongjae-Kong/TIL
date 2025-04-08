def solution(n):
    x = int(n**0.5)  # 제곱근을 정수로 내림
    if x * x == n:   # 제곱해서 원래 수와 같다면 제곱수
        return (x + 1) ** 2
    else:
        return -1
