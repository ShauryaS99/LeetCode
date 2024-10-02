# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # O(n) + O(nlogn)
        col_dict = defaultdict(list)
        q = deque([(root, (0, 0))])
        while q:
            node, (col, row) = q.popleft()
            col_dict[(col, row)].append(node.val)
            if node.left:
                q.append((node.left, (col -1, row +1)))
            if node.right:
                q.append((node.right, (col +1, row +1)))
        col_dict = dict(sorted(col_dict.items()))
        res = []
        prev_col = -float('inf')
        for k,v in col_dict.items():
            col = k[0]
            v.sort()
            if col != prev_col:
                res.append(v)
                prev_col = col
            else:
                res[len(res) - 1].extend(v)
        
        return res
            