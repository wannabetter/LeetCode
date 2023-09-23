from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        self.dict = [-1] * n
        self.kids = [[] for _ in range(n)]
        for index, p in enumerate(parent):
            if p != -1:
                self.kids[p].append(index)

    def lock(self, num: int, user: int) -> bool:
        if self.dict[num] == -1:
            self.dict[num] = user
            return True
        else:
            return False

    def unlock(self, num: int, user: int) -> bool:
        if self.dict[num] == user:
            self.dict[num] = -1
            return True
        else:
            return False

    def hasLockedAncestor(self,num):
        num= self.parent[num]
        while num!=-1:
            if self.dict[num]!=-1:
                return True
            else:
                num=self.parent[num]
        return False

    def checkAndUnlockDescendant(self,num):
        ans = self.dict[num] != -1
        self.dict[num] = -1
        for child in self.kids[num]:
            ans |= self.checkAndUnlockDescendant(child)
        return ans

    def upgrade(self, num: int, user: int) -> bool:
        ans = self.dict[num] == -1 and not self.hasLockedAncestor(num) and self.checkAndUnlockDescendant(num)
        if ans:
            self.dict[num] = user
        return ans
