# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #in recursion, you need to satisfy the base cases (the end of traversal, past the leaf nodes)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        #if both values are equal you go through with the recursion so you can fail/ succeed later
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
                        
            