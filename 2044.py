from typing import List


def countMaxOrSubsets(nums: List[int]) -> int:
    SumTimes = 0
    Temp = []

    def GetOr(Lists):
        Sum = Lists[0]
        for Item in Lists:
            Sum = Sum | Item
        return Sum

    Max = GetOr(nums)

    def BackTrace(Index):
        nonlocal SumTimes
        if Index == len(nums):
            if Temp != [] and Max == GetOr(Temp[:]):
                print(Temp, GetOr(Temp[:]))
                SumTimes += 1
            return
        Temp.append(nums[Index])
        BackTrace(Index + 1)
        Temp.pop()
        BackTrace(Index + 1)

    BackTrace(0)
    return SumTimes


if __name__ == "__main__":
    print(countMaxOrSubsets([3, 2, 1, 5]))
