# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS method that will update a good_counter var
        def dfs(node, max_val, good_counter):
            if node:
                if node.val >= max_val:
                    good_counter += 1
                    max_val = node.val
                # Must update good_counter var as we come back from left branch
                good_counter = dfs(node.left, max_val, good_counter)
                good_counter = dfs(node.right, max_val, good_counter)
            return good_counter
        good_counter = dfs(root, root.val, 0)
        return good_counter