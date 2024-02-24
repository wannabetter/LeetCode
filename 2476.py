from typing import Optional, List
from bisect import bisect_left

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closestNodes(root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
    arr = []

    def DFS(node):
        if not node:
            return
        DFS(node.left)
        arr.append(node.val)
        DFS(node.right)

    DFS(root)

    ans = []

    for query in queries:
        minVal, maxVal = -1, -1
        index = bisect_left(arr, query)
        if index != len(arr):
            maxVal = arr[index]
            if arr[index] == query:
                minVal = arr[index]
                ans.append([minVal, maxVal])
                continue
        if index != 0:
            minVal = arr[index - 1]
        ans.append([minVal, maxVal])

    return ans

