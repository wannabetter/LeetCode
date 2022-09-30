from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    QueueI, QueueJ = [], []
    for IndexI in range(len(matrix)):
        for IndexJ in range(len(matrix[0])):
            if matrix[IndexI][IndexJ] == 0:
                QueueI.append(IndexI)
                QueueJ.append(IndexJ)

    while QueueI:
        X, Y = QueueI.pop(0), QueueJ.pop(0)
        for index in range(len(matrix)):
            matrix[index][Y] = 0
        for index in range(len(matrix[0])):
            matrix[X][index] = 0
