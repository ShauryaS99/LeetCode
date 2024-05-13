# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #O(logN) time complexity
        def binary_search(node):
            if not node:
                return
            if node.val < val:
                return binary_search(node.right)
            elif node.val > val:
                return binary_search(node.left)
            else:
                return node
        return binary_search(root)
