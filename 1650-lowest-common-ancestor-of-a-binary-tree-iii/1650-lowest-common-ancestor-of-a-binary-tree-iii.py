"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
from collections import deque
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_ancestors = set()
        # Add p's ancestors
        while p:
            p_ancestors.add(p.val)
            p = p.parent
        
        # Go through q's ancestors: find common ancestor and return
        while q:
            if q.val in p_ancestors:
                return q
            else:
                q = q.parent
        
        return None