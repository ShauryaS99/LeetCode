# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # O(n)
        max_sum = root.val
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # Recurse on Left subtree
            left = max(dfs(node.left), 0)
            # Recurse on right subtree
            right = max(dfs(node.right), 0)
            
            # Max sum going through current node
            curr_sum = node.val + left + right
            max_sum = max(max_sum, curr_sum)
            
            # Return up to parent node max path (path being 1 direction [no splits])
            return node.val + max(left, right)
        
        dfs(root)
        return max_sum
