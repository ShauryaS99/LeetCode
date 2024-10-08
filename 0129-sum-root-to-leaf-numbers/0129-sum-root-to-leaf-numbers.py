# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #O(n) w/ O(1) space complexity
        if not root:
            return 0
        
        tot_paths = 0
        def dfs(node, curr_path):
            nonlocal tot_paths
            if node:
                # If child node, add val and append path
                if not node.left and not node.right:
                    curr_path += str(node.val)
                    tot_paths += int(curr_path)
                # Else keep going until child node
                else:
                    if node.left:
                        dfs(node.left, curr_path + str(node.val))
                    if node.right:
                        dfs(node.right, curr_path + str(node.val))
            
                
        
        dfs(root, '')
        return tot_paths