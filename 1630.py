from typing import List


def checkArithmeticSubarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    res = []

    for left, right in zip(l, r):
        minItem, maxItem = min(nums[left:right + 1]), max(nums[left: right + 1])
        if maxItem == minItem:
            res.append(True)
            continue
        if (maxItem - minItem) % (right - left) != 0:
            res.append(False)
            continue

        seen = set()
        d = (maxItem - minItem) // (right - left)
        flag = True
        for index in range(left, right + 1):
            if (nums[index] - minItem) % d != 0:
                flag = False
                break
            t = (nums[index] - minItem) // d
            if t in seen:
                flag = False
                break
            seen.add(t)
        res.append(flag)
    return res
