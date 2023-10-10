# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # root, left subtree, right subtree
        res = []
        stack = []
        curr = root
        #stack is good for backtracking: 
        # -- useful for going to leaves and coming back up to the root
        while stack or curr:
            if curr:
                stack.append(curr)
                res.append(curr.val)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right
        return res
            
            