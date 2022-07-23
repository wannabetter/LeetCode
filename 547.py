from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    Res = 0
    Flag = [0 for _ in range(len(isConnected[0]))]

    def DFS(High: int):
        for j in range(len(isConnected)):
            if isConnected[High][j] == 1 and Flag[j] == 0:
                Flag[j] = 1
                DFS(j)

    for item in range(len(isConnected)):
        if Flag[item] == 0:
            DFS(item)
            Res += 1

    return Res


if __name__ == "__main__":
    print(findCircleNum(
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    ))
