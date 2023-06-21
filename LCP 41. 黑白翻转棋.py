from typing import List
from collections import deque


def flipChess(chessboard: List[str]) -> int:
    def taken(board, x, y, offset_x, offset_y):
        x, y = x + offset_x, y + offset_y
        while 0 <= x < len(board) and 0 <= y < len(board[0]):
            if board[x][y] == "X":
                return True
            if board[x][y] == ".":
                return False
            x, y = x + offset_x, y + offset_y
        return False

    def BFS(board, x, y):
        board = [list(row) for row in board]
        cnt = 0
        queue = deque([(x, y)])
        board[x][y] = "X"
        while queue:
            new_x, new_y = queue.popleft()
            for offset_x in [-1, 0, 1]:
                for offset_y in [-1, 0, 1]:
                    if offset_x == 0 and offset_y == 0:
                        continue
                    if taken(board, new_x, new_y, offset_x, offset_y):
                        x, y = new_x + offset_x, new_y + offset_y
                        while board[x][y] != "X":
                            queue.append((x, y))
                            board[x][y] = "X"
                            x, y = x + offset_x, y + offset_y
                            cnt += 1
        return cnt

    res = 0
    for i in range(len(chessboard)):
        for j in range(len(chessboard[0])):
            if chessboard[i][j] == ".":
                res = max(res, BFS(chessboard, i, j))
    return res
