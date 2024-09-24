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
        #O(1) space complexity
        copy_p = p
        copy_q = q
        # Traverse up parent nodes
        while copy_p != copy_q:
            if copy_p:
                copy_p = copy_p.parent
            else:
                # Upon reaching root, switch ptr to OTHER node
                # a+b = b+a => will meet at LCA
                copy_p = q
            if copy_q:
                copy_q = copy_q.parent
            else:
                copy_q = p
        return copy_p