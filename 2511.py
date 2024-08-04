from typing import List


def captureForts(forts: List[int]) -> int:
    ans = 0
    for index, fort in enumerate(forts):
        if fort == 1:
            left, right = 0, 0
            cur = index - 1
            while cur >= 0 and forts[cur] == 0:
                left += 1
                cur -= 1
            if cur < 0 or forts[cur] != -1:
                left = 0
            cur = index + 1
            while cur < len(forts) and forts[cur] == 0:
                right += 1
                cur += 1
            if cur == len(forts) or forts[cur] != -1:
                right = 0
            ans = max(ans, left, right)
    return ans
