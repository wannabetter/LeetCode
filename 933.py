class Node:
    def __init__(self):
        self.val = 0
        self.add = 0

        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self):
        self.root = Node()

    def pull(self, node: Node):
        node.val = node.left.val + node.right.val

    def push(self, node: Node, left: int, right: int):
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()

        if node.add == 0:
            return

        node.left.val += node.add * left
        node.right.val += node.add * right

        node.left.add += node.add
        node.right.add += node.add

        node.add = 0

    def update(self, node: Node, start: int, end: int, left: int, right: int, val: int):
        if left <= start and right >= end:
            node.val += (end - start + 1) * val
            node.add += val
            return

        mid = (start + end) // 2

        self.push(node, mid - start + 1, end - mid)

        if left <= mid:
            self.update(node.left, start, mid, left, right, val)
        if right > mid:
            self.update(node.right, mid + 1, end, left, right, val)

        self.pull(node)

    def query(self, node: Node, start: int, end: int, left: int, right: int):
        if left <= start and right >= end:
            return node.val

        mid = (start + end) // 2

        self.push(node, mid - start + 1, end - mid)

        ans = 0
        if left <= mid:
            ans += self.query(node.left, start, mid, left, right)
        if right > mid:
            ans += self.query(node.right, mid + 1, end, left, right)

        return ans


class RecentCounter:

    def __init__(self):
        self.tree = SegmentTree()

    def ping(self, t: int) -> int:
        self.tree.update(self.tree.root, 3001, 10 ** 9 + 3000, t + 3000, t + 3000, 1)
        return self.tree.query(self.tree.root, 3001, 10 ** 9 + 3000, t, t + 3000)
