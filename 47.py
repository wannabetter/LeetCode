from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    Res = []

    def BackTrace(Index):
        if Index == len(nums):
            if nums[:] not in Res:
                Res.append(nums[:])
            return

        for i in range(Index, len(nums)):
            nums[i], nums[Index] = nums[Index], nums[i]
            BackTrace(Index + 1)
            nums[Index], nums[i] = nums[i], nums[Index]

    BackTrace(0)
    return Res


if __name__=="__main__":
    print(permuteUnique([1,1,2]))