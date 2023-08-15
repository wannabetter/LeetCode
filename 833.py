from typing import List


def findReplaceString(s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
    ops = list(range(len(indices)))
    ops.sort(key=lambda index: indices[index])

    offset = 0
    for index in ops:
        strs, length = sources[index], len(sources[index])
        target, length_target = targets[index], len(targets[index])
        if s[indices[index] + offset:indices[index] + offset + length] == strs:
            s = s[:indices[index] + offset] + target + s[indices[index] + offset + length:]
            offset += length_target - length
    return s
