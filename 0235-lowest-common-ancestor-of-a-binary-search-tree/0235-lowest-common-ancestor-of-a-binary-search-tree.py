# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #O(logn)
        def dfs(node):
            if node:
                # Node val is greater than both => go left
                if node.val > p.val and node.val > q.val:
                    return dfs(node.left)
                elif node.val < p.val and node.val < q.val:
                    return dfs(node.right)
                else:
                    return node
                    
        
        lca = dfs(root)
        return lca