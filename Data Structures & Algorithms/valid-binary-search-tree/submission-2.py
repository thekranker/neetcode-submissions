# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(root: Optional[TreeNode], low: int, high: int):
            
            if not root:
                return True
            
            if not (root.val > low and root.val < high):
                return False

            if not dfs(root.left, low, root.val) or not dfs(root.right, root.val, high):
                return False
            
            return True

        return dfs(root, float('-inf'), float('inf'))
        