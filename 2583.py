from typing import Optional
from heapq import heappop, heappush


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthLargestLevelSum(root: Optional[TreeNode], k: int) -> int:
    heap = []
    queue = [root]
    while queue:
        nodeSum = 0
        temp = queue
        queue = []
        while temp:
            node = temp.pop(0)
            nodeSum = nodeSum + node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        heappush(heap, nodeSum)
    heap.sort()
    return -1 if len(heap) < k else heap[-k]