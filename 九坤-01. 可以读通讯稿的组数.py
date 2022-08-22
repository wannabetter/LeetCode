from typing import List
from collections import Counter


def numberOfPairs(nums: List[int]) -> int:
    Cnt = Counter()
    SumPairs = 0

    def GetRes(Num):
        Sum = 0
        while Num:
            Sum = Sum * 10 + Num % 10
            Num = Num // 10
        return Sum

    for item in nums:
        ResNum = GetRes(item)
        Cnt[ResNum - item] += 1
        if Cnt[ResNum - item] >= 2:
            SumPairs += Cnt[ResNum - item] - 1

    return SumPairs % (10 ** 9 + 7)


if __name__ == "__main__":
    print(numberOfPairs([17, 28, 39, 71]))
