# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #O(n) runtime, O(1) space
        max_edges = 0
        def dfs(node):
            nonlocal max_edges
            # Come back up
            if not node:
                return 0
            # Child node
            if not node.left and not node.right:
                return 1
            
            # Update max path going through curr node as root
            left_edges = dfs(node.left)
            right_edges = dfs(node.right)
            max_edges = max(max_edges, left_edges + right_edges)
            
            # Traverse up one level, taking longest path2child
            return 1 + max(left_edges, right_edges)
                
        
        dfs(root)
        return max_edges
            
