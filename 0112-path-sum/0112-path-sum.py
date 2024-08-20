# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # O(n)
        if not root:
            return False
        
        def dfs(node, curr_sum):
            if not node:
                return False
            
            curr_sum += node.val
            
            # Reached a leaf node
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return True
                else:
                    return False
                
            # Continue traversing tree, accumulating sums
            path1 = dfs(node.left, curr_sum)
            path2 = dfs(node.right, curr_sum)
            return path1 or path2

        return dfs(root, 0)