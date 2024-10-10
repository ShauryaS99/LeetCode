# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_order = defaultdict(list)
        def dfs(node, col, row):
            if node:
                col_order[(col, row)].append(node.val)
                dfs(node.left, col - 1, row + 1)
                dfs(node.right, col + 1, row + 1)
        dfs(root, 0, 0)
        col_order = dict(sorted(col_order.items()))
        res = []
        prev_col = -float('inf')
        for k, v in col_order.items():
            col = k[0]
            row = k[1]
            if col == prev_col:
                res[-1].extend(v)
            else:
                prev_col = col
                res.append(v)
        return res
        
                