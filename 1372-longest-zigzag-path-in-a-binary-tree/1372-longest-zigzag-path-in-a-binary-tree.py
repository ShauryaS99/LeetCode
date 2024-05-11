# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0
        #DFS exploring all nodes
        def dfs(node, curr_path, direction):
            if node:
                if direction == 'left':
                    # Reset counter if we repeat direction
                    dfs(node.right, curr_path + 1, 'right')
                    dfs(node.left, 0, 'left')
                if direction == 'right':
                    # Reset counter if we repeat direction
                    dfs(node.left, curr_path + 1, 'left')
                    dfs(node.right, 0, 'right')
            # Update path once we reach leaf
            self.longest_path = max(curr_path, self.longest_path)
        dfs(root.left, 0, 'left')
        dfs(root.right, 0, 'right')
        return self.longest_path