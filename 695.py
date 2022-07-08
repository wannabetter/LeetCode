from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    Max = 0
    X = 0
    while X < len(grid):
        Y = 0
        while Y < len(grid[0]):
            if grid[X][Y] == 1:
                Temp = 0
                QueueRows = []
                QueueCols = []
                QueueRows.append(X)
                QueueCols.append(Y)
                print(QueueRows, QueueCols)
                while QueueRows:
                    Row = QueueRows.pop(0)
                    Col = QueueCols.pop(0)
                    print(QueueRows, QueueCols)
                    grid[Row][Col] = 0
                    Temp += 1
                    if Row + 1 < len(grid) and grid[Row + 1][Col] == 1:
                        QueueRows.append(Row + 1)
                        QueueCols.append(Col)
                        grid[Row + 1][Col] = 0
                    if Col + 1 < len(grid[0]) and grid[Row][Col + 1] == 1:
                        QueueRows.append(Row)
                        QueueCols.append(Col + 1)
                        grid[Row][Col+1] = 0
                    if Col - 1 >= 0 and grid[Row][Col - 1] == 1:
                        QueueRows.append(Row)
                        QueueCols.append(Col - 1)
                        grid[Row][Col-1] = 0
                    if Row - 1 >= 0 and grid[Row - 1][Col] == 1:
                        QueueRows.append(Row - 1)
                        QueueCols.append(Col)
                        grid[Row-1][Col] = 0
                Max = max(Max, Temp)
            Y += 1
        X += 1
    return Max


if __name__ == "__main__":
    print(maxAreaOfIsland(grid=[[1, 1, 0, 0, 0],
                                [1, 1, 0, 0, 0],
                                [0, 0, 0, 1, 1],
                                [0, 0, 0, 1, 1]]))
