from math import inf
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largestValues(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    else:
        ans = []
        Queue = [root]
        while Queue:
            MaxVal = -inf
            Temps = Queue
            Queue = []
            for Temp in Temps:
                if Temp.val > MaxVal:
                    MaxVal = Temp.val
                if Temp.left:
                    Queue.append(Temp.left)
                if Temp.right:
                    Queue.append(Temp.right)
            ans.append(MaxVal)
        return ans