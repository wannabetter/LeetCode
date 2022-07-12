from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    Res = [[triangle[0][0]]]
    for index in range(1, len(triangle)):
        Ans = [Res[index - 1][0] + triangle[index][0]]
        for col in range(1, index):
            Ans.append(min(Res[index - 1][col - 1], Res[index - 1][col])+triangle[index][col])
        Ans.append(Res[index - 1][-1]+triangle[index][-1])
        Res.append(Ans)
    print(Res)
    return min(Res[-1])
