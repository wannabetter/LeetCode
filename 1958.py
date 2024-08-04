from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:

        def check(dx, dy):
            step = 1
            x, y = rMove + dx, cMove + dy

            while 0 <= x < 8 and 0 <= y < 8:
                if step == 1:
                    if board[x][y] == color or board[x][y] == '.':
                        return False
                else:
                    if board[x][y] == '.':
                        return False
                    if board[x][y] == color:
                        return True

                step = step + 1
                x = x + dx
                y = y + dy

            return False

        dx = [-1, 1, 0, 0, -1, 1, 1, -1]
        dy = [0, 0, -1, 1, -1, 1, -1, 1]

        for x, y in zip(dx, dy):
            if check(x, y):
                return True
        return False

