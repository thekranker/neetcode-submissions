# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # nested function, takes in root node, returns an int
        # looks at the left and right subtrees, and validates that they are
        # height-balanced
        # if they aren't height balanced, it would return -1
        def checkBalance(root: Optional[TreeNode]) -> int:

            if not root:
                return 0
            
            leftHeight = 1 + checkBalance(root.left)
            rightHeight = 1 + checkBalance(root.right)

            if leftHeight == 0 or rightHeight == 0 or abs(leftHeight - rightHeight) > 1:
                return -1
            
            return max(leftHeight, rightHeight)



        # if when the nested function is called and the output is -1, return false, else true
        if checkBalance(root) == -1:
            return False

        return True





