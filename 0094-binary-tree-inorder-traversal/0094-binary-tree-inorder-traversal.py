# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #rules
    #go left as much as possible
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        # you need stack or curr b/c stack is empty once you go to right subtree
        while stack or curr:
            # go all the way left until it is null
            while curr:
                stack.append(curr)
                curr = curr.left
            # get the last on the stack --> process and go right
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
            
            