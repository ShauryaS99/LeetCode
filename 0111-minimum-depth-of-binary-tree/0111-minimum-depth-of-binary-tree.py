# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # O(n): DFS approach
        if not root:
            return 0
        
        min_depth = float('inf')
        def dfs(node, curr_depth):
            nonlocal min_depth
            # Increment depth as we traverse paths
            if node.left:
                dfs(node.left, curr_depth + 1)
            if node.right: 
                dfs(node.right, curr_depth + 1)
                
            # If we reach leaf: measure depth
            if not node.left and not node.right:
                min_depth = min(min_depth, curr_depth)
                
        dfs(root, 1)
        return min_depth