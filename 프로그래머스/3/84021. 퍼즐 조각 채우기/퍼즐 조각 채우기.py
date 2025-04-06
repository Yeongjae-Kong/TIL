from collections import deque

def solution(game_board, table):
    n = len(game_board)

    def get_shapes(board, target):
        visited = [[False]*n for _ in range(n)]
        shapes = []

        for i in range(n):
            for j in range(n):
                if board[i][j] == target and not visited[i][j]:
                    queue = deque([(i, j)])
                    visited[i][j] = True
                    shape = []
                    while queue:
                        x, y = queue.popleft()
                        shape.append((x, y))
                        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                            nx, ny = x+dx, y+dy
                            if 0<=nx<n and 0<=ny<n and board[nx][ny] == target and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                    shapes.append(normalize(shape))
        return shapes

    def normalize(shape):
        min_x = min([x for x, y in shape])
        min_y = min([y for x, y in shape])
        return sorted([(x - min_x, y - min_y) for x, y in shape])

    def rotate(shape):
        return normalize([ (y, -x) for x, y in shape ])

    puzzle_pieces = get_shapes(table, 1)
    empty_spaces = get_shapes(game_board, 0)

    used = [False] * len(puzzle_pieces)
    answer = 0

    for empty in empty_spaces:
        matched = False
        for i in range(len(puzzle_pieces)):
            if used[i]:
                continue
            puzzle = puzzle_pieces[i]
            for _ in range(4):
                if empty == puzzle:
                    used[i] = True
                    answer += len(puzzle)
                    matched = True
                    break
                puzzle = rotate(puzzle)
            if matched:
                break

    return answer
