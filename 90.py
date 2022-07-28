from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    Res = []
    Temp = []

    def BinTrace(Index):
        if Index == len(nums):
            Ans = Temp[:]
            Ans.sort()
            if Ans not in Res:
                Res.append(Ans)
            return

        Temp.append(nums[Index])
        BinTrace(Index + 1)
        Temp.pop()
        BinTrace(Index + 1)

    BinTrace(0)

    return Res


if __name__ == "__main__":
    print(subsetsWithDup([4, 4, 4, 1, 4]))
