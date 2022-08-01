from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    Flag = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    print(Flag)

    def DFS(X, Y, Length):
        print(X, Y, Length)
        Res = False
        if Length == len(word) - 1:
            return True
        if X + 1 < len(board) and board[X + 1][Y] == word[Length + 1] and not Flag[X + 1][Y]:
            Flag[X + 1][Y] = True
            Res = DFS(X + 1, Y, Length + 1) or Res
            Flag[X + 1][Y] = False
        if Y + 1 < len(board[0]) and board[X][Y + 1] == word[Length + 1] and not Flag[X][Y + 1]:
            Flag[X][Y + 1] = True
            Res = DFS(X, Y + 1, Length + 1) or Res
            Flag[X][Y + 1] = False
        if 0 <= X - 1 and board[X - 1][Y] == word[Length + 1] and not Flag[X - 1][Y]:
            Flag[X - 1][Y] = True
            Res = DFS(X - 1, Y, Length + 1) or Res
            Flag[X - 1][Y] = False
        if 0 <= Y - 1 and board[X][Y - 1] == word[Length + 1] and not Flag[X][Y - 1]:
            Flag[X][Y - 1] = True
            Res = DFS(X, Y - 1, Length + 1) or Res
            Flag[X][Y - 1] = False

        return Res

    for Row in range(len(board)):
        for Col in range(len(board[0])):
            if board[Row][Col] == word[0]:
                Flag[Row][Col] = True
                if DFS(Row, Col, 0):
                    return True
                Flag[Row][Col] = False
    return False


if __name__ == "__main__":
    print(exist([["A", "A", "A", "A", "A", "A"],
                 ["A", "A", "A", "A", "A", "A"],
                 ["A", "A", "A", "A", "A", "A"],
                 ["A", "A", "A", "A", "A", "A"],
                 ["A", "A", "A", "A", "A", "B"],
                 ["A", "A", "A", "A", "B", "A"]], "AAAAAAAAAAAAABB"))
