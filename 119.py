from typing import List


def getRow(rowIndex: int) -> List[int]:
    triangle = [[1], [1, 1]]
    for i in range(2, rowIndex+1):
        pre = triangle[i - 1]
        cul = [1]
        for j in range(i - 1):
            cul.append(pre[j] + pre[j + 1])
        cul.append(1)
        triangle.append(cul)
    print(triangle)
    return triangle[rowIndex]


if __name__ == "__main__":
    print(getRow(3))
