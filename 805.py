from typing import List


def splitArraySameAverage(nums: List[int]) -> bool:
    n = len(nums)
    if n == 1:
        return False

    s = sum(nums)
    for i in range(n):
        nums[i] = nums[i] * n - s

    m = n // 2
    left = set()
    for i in range(1, 1 << m):
        tot = sum(x for j, x in enumerate(nums[:m]) if i >> j & 1)
        if tot == 0:
            return True
        left.add(tot)

    rsum = sum(nums[m:])
    for i in range(1, 1 << (n - m)):
        tot = sum(x for j, x in enumerate(nums[m:]) if i >> j & 1)
        if tot == 0 or rsum != tot and -tot in left:
            return True
    return False


if __name__ == '__main__':
    print(splitArraySameAverage([3,1]))
