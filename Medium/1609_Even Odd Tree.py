from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q = deque([root])
        level = 0
        while q:
            size = len(q)
            prev_val = None if level % 2 == 0 else float('inf')
            for _ in range(size):
                node = q.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val):
                        return False
                else:
                    if node.val % 2 != 0 or (prev_val is not None and node.val >= prev_val):
                        return False
                prev_val = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True