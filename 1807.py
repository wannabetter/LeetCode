from typing import List


def evaluate(s: str, knowledge: List[List[str]]) -> str:
    d, start, ans = dict(knowledge), -1, []
    for index, char in enumerate(s):
        if char == "(":
            start = index
        elif char == ")":
            ans.append(d.get(s[start + 1: index], "?"))
            start = -1
        elif start < 0:
            ans.append(char)
    return "".join(ans)
