from typing import List


def getFolderNames(names: List[str]) -> List[str]:
    res = []
    Hash = {}
    for name in names:
        if name not in Hash:
            res.append(name)
            Hash[name] = 1
        else:
            index = Hash[name]
            newName = name + "(" + str(index) + ")"
            while newName in Hash:
                index += 1
                newName = name + "(" + str(index) + ")"
            res.append(newName)
            Hash[newName] = 1
            Hash[name] = index + 1
    return res