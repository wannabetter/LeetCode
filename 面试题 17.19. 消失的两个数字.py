from typing import List
import math


def missingTwo(nums: List[int]) -> List[int]:
    n = len(nums) + 2
    Sum = sum(nums)
    Sum1 = (1 + n) * n / 2
    a = Sum1 - Sum
    Sum, Sum1 = 0, 0
    for num in nums:
        Sum += num ** 2
    for index in range(1, n + 1):
        Sum1 += index ** 2
    b = Sum1 - Sum
    tmp = math.sqrt(2 * b - a * a)
    return [int((a+tmp)/2),int((a-tmp)/2)]


if __name__ == '__main__':
    print(missingTwo([2]))
