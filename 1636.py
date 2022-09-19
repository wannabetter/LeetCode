from typing import List
from collections import Counter


def frequencySort(nums: List[int]) -> List[int]:
    cnt = Counter(nums)
    nums.sort(key=lambda x: (cnt[x], -x))
    return nums


if __name__ == '__main__':
    print(frequencySort([2, 3, 1, 3, 2]))
