# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue = [[p,q]]

        while queue:
            nodeOne, nodeTwo = queue.pop(0)

            # base cases
            if not nodeOne and not nodeTwo:
                continue
            if not nodeOne and nodeTwo or nodeOne and not nodeTwo:
                return False
            if not nodeOne.val == nodeTwo.val:
                return False

            queue.append([nodeOne.left, nodeTwo.left]) # left subtrees
            queue.append([nodeOne.right, nodeTwo.right]) # right subtrees



        return True
        