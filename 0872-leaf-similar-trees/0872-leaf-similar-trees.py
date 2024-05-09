# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # DFS on both trees
        def recurse(node, leaf_value_lst):
            if node:
                if not node.left and not node.right:
                    leaf_value_lst.append(node.val)
                recurse(node.left, leaf_value_lst)
                recurse(node.right, leaf_value_lst)
            return leaf_value_lst
        leaf_value_1 = recurse(root1, [])
        leaf_value_2 = recurse(root2, [])
        # Runtime: O(n), n being the nodes in the tree
        return leaf_value_1 == leaf_value_2
        