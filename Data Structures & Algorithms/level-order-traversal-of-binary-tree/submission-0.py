# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []
        queue = deque()

        if not root:
            return output

        queue.append(root)

        while queue:
            levelSize = len(queue)
            tempOutput = []
            for i in range(levelSize):
                node = queue.popleft()
                tempOutput.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            output.append(tempOutput)

        return output
        