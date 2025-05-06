def solution(info, n, m):
    from collections import deque

    max_len = len(info)
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True

    # (A_trace_sum, B_trace_sum)
    q = deque()
    q.append((0, 0))

    for a_i, b_i in info:
        next_visited = [[False]*m for _ in range(n)]
        next_q = deque()

        while q:
            a, b = q.popleft()
            # A가 맡을 경우
            na, nb = a + a_i, b
            if na < n and not next_visited[na][nb]:
                next_visited[na][nb] = True
                next_q.append((na, nb))
            # B가 맡을 경우
            na, nb = a, b + b_i
            if nb < m and not next_visited[na][nb]:
                next_visited[na][nb] = True
                next_q.append((na, nb))

        visited = next_visited
        q = next_q

    # 가능한 상태 중 최소 A 흔적 누적 합 찾기
    for a in range(n):
        for b in range(m):
            if visited[a][b]:
                return a
    return -1
