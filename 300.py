from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    Res = []
    for Item in range(0, len(nums)):
        Res.append(1)
        for Index in range(Item, -1, -1):
            if nums[Item] > nums[Index]:
                Res[Item] = max(Res[Index] + 1, Res[Item])

    return max(Res)


if __name__ == "__main__":
    print(lengthOfLIS([10,9,2,5,3,7,101,18]))
