from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    Sum = 0
    Temp = []
    for I in range(len(grid)):
        T = [grid[J][I] for J in range(len(grid))]
        Temp.append(T)
    for I in range(len(grid)):
        for J in range(len(grid)):
            if Temp[J] == grid[I]:
                Sum += 1
    return Sum


if __name__ == "__main__":
    print(equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
