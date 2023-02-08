from typing import List


def removeSubfolders(folder: List[str]) -> List[str]:
    folder.sort()
    ans = [folder[0]]
    for index in range(1, len(folder)):
        m, n = len(ans[-1]), len(folder[index])
        if m >= n or not (folder[index][:m] == ans[-1] and folder[index][m] == "/"):
            ans.append(folder[index])
    return ans
