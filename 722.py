from typing import List


def removeComments(source: List[str]) -> List[str]:
    ans = []
    new_line = []
    in_block = False
    for line in source:
        index = 0
        while index < len(line):
            if in_block:
                if index + 1 < len(line) and line[index] == "*" and line[index + 1] == "/":
                    in_block = False
                    index = index + 1
            else:
                if index + 1 < len(line) and line[index] == "/" and line[index + 1] == "*":
                    in_block = True
                    index = index + 1
                elif index + 1 < len(line) and line[index] == "/" and line[index + 1] == "/":
                    break
                else:
                    new_line.append(line[index])
            index = index + 1
        if not in_block and len(new_line) > 0:
            ans.append("".join(new_line))
            new_line = []
    return ans
