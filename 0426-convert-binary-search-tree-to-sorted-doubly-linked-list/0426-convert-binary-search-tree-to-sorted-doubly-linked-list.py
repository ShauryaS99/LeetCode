"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #O(n) time complexity O(1) space complexity
        if not root:
            return None
        
        low = None
        high = None
        
        #Inorder traversal of BST is sorted!
        def dfs(node):
            nonlocal low, high
            if node:
                dfs(node.left)
                # Insert node 
                if high:
                    high.right = node
                    node.left = high
                # First time high DNE, is lowest node --> set low
                else:
                    low = node
                # Set highest node seen till that point
                high = node
                dfs(node.right)
        
        dfs(root)
        low.left = high
        high.right = low
        return low