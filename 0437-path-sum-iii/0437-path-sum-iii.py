# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.num_paths = 0
        # Method to count all values going down from a START_node
        def pathTotal(node, curr_sum):
            curr_sum += node.val
            if curr_sum == targetSum:
                self.num_paths += 1
            if node.left:
                pathTotal(node.left, curr_sum)
            if node.right:
                pathTotal(node.right, curr_sum)
        # Call pathTotal from every node
        def dfs(node):
            if node:
                pathTotal(node, 0)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        # Brute force solution: DFS from every node O(n^2)
        return self.num_paths
