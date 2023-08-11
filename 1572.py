from typing import List


def diagonalSum(mat: List[List[int]]) -> int:
    ans = 0
    for index_x in range(len(mat)):
        for index_y in range(len(mat[0])):
            if index_x == index_y:
                ans += mat[index_x][index_y]
                print(mat[index_x][index_y])
            elif index_x + index_y == len(mat[0]) - 1:
                ans += mat[index_x][index_y]
                print(mat[index_x][index_y])
    return ans