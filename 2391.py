from typing import List


def garbageCollection(garbage: List[str], travel: List[int]) -> int:
    M, P, G = -1, -1, -1
    Res = [[0 for _ in range(len(garbage))] for _ in range(3)]

    for index, chars in enumerate(garbage):
        for char in chars:
            if char == "M":
                Res[0][index] += 1
                M = index
            if char == "P":
                Res[1][index] += 1
                P = index
            if char == "G":
                Res[2][index] += 1
                G = index
        if index < len(travel):
            Res[0][index + 1] += Res[0][index] + travel[index]
            Res[1][index + 1] += Res[1][index] + travel[index]
            Res[2][index + 1] += Res[2][index] + travel[index]
    Sum = 0
    for index, item in enumerate([M, P, G]):
        if item >= 0:
            Sum += Res[index][item]

    return Sum


if __name__ == "__main__":
    print(garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]))
