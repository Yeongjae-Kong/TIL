def solution(n, times):
    start, end, mid = 1, times[-1]*n, 0
    
    while start < end:
        mid = (start+end) // 2
        total = 0
        for t in times:
            total += mid // t
        if n <= total:
            end = mid
        else:
            start = mid+1
    return start