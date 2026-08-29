# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # needs bfs, only pick the last element in the queue
        # need an output array

        output = []
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            currLen = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                if i == currLen - 1:
                    output.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return output
                
            

        