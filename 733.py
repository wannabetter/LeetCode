from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    Val = image[sr][sc]
    QueueRow = [sr]
    QueueCol = [sc]
    Rows, Cols = len(image), len(image[0])
    if Val == color:
        return image

    while len(QueueRow) != 0:
        Row = QueueRow.pop(0)
        Col = QueueCol.pop(0)
        image[Row][Col] = color
        if Row + 1 < Rows and image[Row + 1][Col] == Val:
            QueueRow.append(Row + 1)
            QueueCol.append(Col)
        if Col + 1 < Cols and image[Row][Col + 1] == Val:
            QueueRow.append(Row)
            QueueCol.append(Col + 1)
        if Col - 1 >= 0 and image[Row][Col - 1] == Val:
            QueueRow.append(Row)
            QueueCol.append(Col - 1)
        if Row - 1 >= 0 and image[Row - 1][Col] == Val:
            QueueRow.append(Row - 1)
            QueueCol.append(Col)
    return image
