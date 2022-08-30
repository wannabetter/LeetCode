from typing import List


def answerQueries(nums: List[int], queries: List[int]) -> List[int]:
    Res = []
    for query in queries:
        Temp = query
        LenSub = 0
        for num in nums:
            if Temp >= num:
                Temp -= num
                LenSub += 1
        Res.append(LenSub)
    return Res
