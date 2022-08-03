from typing import List
from math import inf


def jump(nums: List[int]) -> int:
    Res = [inf] * len(nums)
    Res[0] = 0

    for Index, Jumps in enumerate(nums):
        for Jump in range(1, Jumps + 1):
            if Jump + Index < len(nums):
                Res[Jump + Index] = min(Res[Jump + Index], Res[Index] + 1)

    return Res[-1]


if __name__ == "__main__":
    print(jump([2, 3, 0, 1, 4]))
