# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #need to pass bounds because of case [5,4,6,null,null,3,7] 
        def isValidBSTHelper(root, lower_bound, upper_bound):
            if not root:
                return True
            #if root.val is outside of bounds return false
            if (root.val >= upper_bound or root.val <= lower_bound):
                return False
            #if all conditions succeed keep recursing
            return (isValidBSTHelper(root.left, lower_bound, root.val) and isValidBSTHelper(root.right, root.val, upper_bound))
        return isValidBSTHelper(root, float('-inf'), float('inf'))
    