# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))
    def isValidBSTHelper(self, root, lower_bound, upper_bound):
        if not root:
            return True
        if root.left and (root.left.val >= root.val or root.left.val <= lower_bound):
            return False
        if root.right and (root.right.val <= root.val or root.right.val >= upper_bound):
            return False
        return (self.isValidBSTHelper(root.left, lower_bound, root.val) and self.isValidBSTHelper(root.right, root.val, upper_bound))