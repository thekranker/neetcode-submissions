# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxDiameter = 0

        def calcDepths(root: Optional[TreeNode]) -> int:
            nonlocal maxDiameter
            if not root:
                return 0

            leftDepth = calcDepths(root.left)
            rightDepth = calcDepths(root.right)
            # add the depths up
            diameter = leftDepth + rightDepth

            # compare to current max diameter, keep the max
            maxDiameter = max(maxDiameter, diameter)
            return 1 + max(leftDepth, rightDepth)
        
        calcDepths(root)


        # return the max diameter
        return maxDiameter