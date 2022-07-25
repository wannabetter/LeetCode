from typing import List
import copy


def subsets(nums: List[int]) -> List[List[int]]:
    Res = []
    Temp = []

    def BackTrace(Index):
        if Index == len(nums):
            Res.append(Temp[:])
            return
        Temp.append(nums[Index])
        BackTrace(Index + 1)
        Temp.pop()
        BackTrace(Index + 1)

    BackTrace(0)

    return Res


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
