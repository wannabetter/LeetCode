from typing import List


def lakeCount(field: List[str]) -> int:
    Sum, QueueI, QueueJ = 0, [], []
    for IndexI in range(len(field)):
        for IndexJ in range(len(field[0])):
            Temp = field[IndexI]
            if Temp[IndexJ] == "W":
                QueueI.append(IndexI)
                QueueJ.append(IndexJ)
                while QueueI:
                    print(field)
                    X, Y = QueueI.pop(0), QueueJ.pop(0)
                    Temp = field[X]
                    Chars = Temp[:Y] + "." + Temp[Y + 1:]
                    field[X] = Chars
                    for UPI, UPJ in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                        if 0 <= X + UPI < len(field) and 0 <= Y + UPJ < len(field[0]) and field[X + UPI][Y + UPJ] == "W":
                            QueueI.append(X + UPI)
                            QueueJ.append(Y + UPJ)
                            Temp = field[X + UPI]
                            Chars = Temp[:Y + UPJ] + "." + Temp[Y + UPJ+1:]
                            field[X + UPI] = Chars
                Sum += 1
    return Sum


if __name__ == "__main__":
    print(lakeCount([".....W", ".W..W.", "....W.", ".W....", "W.WWW.", ".W...."]))
