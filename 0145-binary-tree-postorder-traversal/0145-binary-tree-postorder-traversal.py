# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left subtree, right subtree, root
        res = []
        stack = []
        curr = root
        visited = set()
        #process node once you confirm the right child has been visited
        while stack or curr:
            while curr:
                stack.append(curr)
                visited.add(curr)
                curr = curr.left
            curr = stack[len(stack) - 1]
            #apped res and wait to be popped up a level
            if not curr.right or curr.right in visited:
                curr = stack.pop()
                res.append(curr.val)
                curr = None #don't want to go right again b/c already visisted
            else:
                curr = curr.right
        return res