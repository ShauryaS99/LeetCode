# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #O(nlogn) because of sorting
        if not root:
            return []
        col_order = defaultdict(list)
        q = deque([])
        q.append((root, 0))
        while q:
            node, col = q.popleft()
            col_order[col].append(node.val)
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        #-2: [4], -1: [9], 0: [3, 0, 1]
        col_order = dict(sorted(col_order.items()))
        return col_order.values()
            