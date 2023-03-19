from collections import deque


def findLexSmallestString(s: str, a: int, b: int) -> str:
    vis = {s}
    ans = s
    queue = deque([s])
    while queue:
        s = queue.popleft()
        if ans > s:
            ans = s
        str1 = "".join([str((int(char) + a) % 10) if index & 1 else char for index, char in enumerate(s)])
        str2 = s[-b:] + s[:-b]
        print(str1)
        for char in (str1, str2):
            if char not in vis:
                vis.add(char)
                queue.append(char)
    return ans
