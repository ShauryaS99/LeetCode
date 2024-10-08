# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # O(n): BFS approach
        if not root:
            return 0
        
        q = deque([(root, 1)])
        while q:            
            node, depth = q.popleft()
            
            # We have reached earliest leaf
            if not node.left and not node.right:
                return depth
            
            # Increment depth for every level
            if node.left:
                q.append([node.left, depth + 1])
            if node.right:
                q.append([node.right, depth + 1])
        
        return -1
                
        
        
        