from typing import List


def numIslands(grid: List[List[str]]) -> int:
    Res = 0
    QueueRow = []
    QueueCol = []
    for Row in range(len(grid)):
        for Col in range(len(grid[0])):
            if grid[Row][Col] == "1":
                QueueRow.append(Row)
                QueueCol.append(Col)
                grid[Row][Col] = 0
                while len(QueueRow) != 0:
                    X, Y = QueueRow.pop(0), QueueCol.pop(0)
                    if X - 1 >= 0 and grid[X - 1][Y] == "1":
                        QueueRow.append(X - 1)
                        QueueCol.append(Y)
                        grid[X-1][Y] = "0"
                    if Y - 1 >= 0 and grid[X][Y-1] == "1":
                        QueueRow.append(X)
                        QueueCol.append(Y - 1)
                        grid[X][Y-1] = "0"
                    if X + 1 < len(grid) and grid[X + 1][Y] == "1":
                        QueueRow.append(X + 1)
                        QueueCol.append(Y)
                        grid[X+1][Y] = "0"
                    if Y + 1 < len(grid[0]) and grid[X][Y + 1] == "1":
                        QueueRow.append(X)
                        QueueCol.append(Y + 1)
                        grid[X][Y+1] = "0"
                Res += 1
            else:
                continue
    return Res


if __name__ == "__main__":
    print(numIslands(
        [["1", "1", "1"],
         ["0", "1", "0"],
         ["1", "1", "1"]]))
