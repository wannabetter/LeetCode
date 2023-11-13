from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.Sum = [0] * 4 * len(nums)
        self.CreateSegTree([0] + nums, 1, 1, self.n)

    def CreateSegTree(self, OriNums, Node, L, R):
        if L == R:
            self.Sum[Node] = OriNums[L]
            return
        Mid = (L + R) // 2
        self.CreateSegTree(OriNums, Node * 2, L, Mid)
        self.CreateSegTree(OriNums, Node * 2 + 1, Mid + 1, R)
        self.Sum[Node] = self.Sum[Node * 2] + self.Sum[Node * 2 + 1]

    def Change(self, Node, Index, Val, L, R):
        if L == R:
            self.Sum[Node] = Val
            return
        Mid = (L + R) // 2
        if Index < Mid:
            self.Change(Node * 2, Index, Val, L, Mid)
        else:
            self.Change(Node * 2 + 1, Index, Val, Mid + 1, R)
        self.Sum[Node] = self.Sum[Node * 2] + self.Sum[Node * 2 + 1]

    def Query(self, Node, L, R, QueryL, QueryR):
        # print('L:', L, 'R:', R, 'QueryL:', QueryL, 'QueryR:', QueryR)
        if QueryL <= L and R <= QueryR:
            return self.Sum[Node]
        Mid = (L + R) // 2
        if Mid < QueryL:
            return self.Query(Node * 2 + 1, Mid + 1, R, QueryL, QueryR)
        if Mid >= QueryR:
            return self.Query(Node * 2, L, Mid, QueryL, QueryR)
        return self.Query(Node * 2, L, Mid, QueryL, QueryR) + self.Query(Node * 2 + 1, Mid + 1, R, QueryL, QueryR)

    def update(self, index: int, val: int) -> None:
        self.Change(1, index, val, 1, self.n)

    def sumRange(self, left: int, right: int) -> int:
        return self.Query(1, 1, self.n, left + 1, right + 1)


# ["NumArray","update","sumRange","sumRange","update","sumRange"]
# [[[9,-8]],[0,3],[1,1],[0,1],[1,-3],[0,1]]

if __name__ == '__main__':
    Arr = NumArray([9, -8])
    print(Arr.Sum)
    Arr.update(0, 3)
    print(Arr.Sum)
    print(Arr.sumRange(1, 1))
