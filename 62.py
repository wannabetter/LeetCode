def uniquePaths(m: int, n: int) -> int:
    Res = [[0 for _ in range(n)] for _ in range(m)]

    for Index in range(n):
        Res[0][Index] = 1

    for Index in range(m):
        Res[Index][0] = 1
    print(Res)
    for Row in range(1, m):
        for Col in range(1, n):
            Res[Row][Col] = Res[Row - 1][Col]+Res[Row][Col - 1]
    print(Res)
    return Res[-1][-1]


if __name__ == "__main__":
    print(uniquePaths(3, 7))
    nums = [[1, 1, 1, 1, 1, 1, 1],
            [1, 2, 3, 4, 5, 6, 7],
            [1, 3, 4, 5, 6, 7, 8]]
