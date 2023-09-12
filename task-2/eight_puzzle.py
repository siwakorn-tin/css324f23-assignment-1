import copy

def initial_state():
    return ((7, 2, 4, 5, 0, 6, 8, 3, 1), 1, 1)

def is_goal(s):
    return s[0] == (1, 2, 3, 4, 5, 6, 7, 8, 0)

def successors(s):
    _, r, c = s
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_r, new_c = r + dr, c + dc
        if is_valid(new_r, new_c):
            yield move_blank(s, new_r, new_c), 1

def is_valid(r, c):
    return 0 <= r < 3 and 0 <= c < 3

def move_blank(s, new_r, new_c):
    board, r, c = s
    new_board = list(board)
    index1, index2 = r * 3 + c, new_r * 3 + new_c
    new_board[index1], new_board[index2] = new_board[index2], new_board[index1]
    return (tuple(new_board), new_r, new_c)

def h1(s):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    return sum(1 for i, tile in enumerate(board) if tile != goal[i])

def h3(s):
    board, _, _ = s
    res = 0
    for i, tile in enumerate(board):
        if tile == 0:
            q2, r2 = 2, 2
        else:
            q2, r2 = (tile - 1) // 3, (tile - 1) % 3
        q1, r1 = i // 3, i % 3
        res += abs(q1 - q2) + abs(r1 - r2)
    return res
