from typing import List


def countSeniors(details: List[str]) -> int:
    ans = 0
    for detail in details:
        if int(detail[-4] + detail[-3]) > 60:
            ans += 1
    return ans
