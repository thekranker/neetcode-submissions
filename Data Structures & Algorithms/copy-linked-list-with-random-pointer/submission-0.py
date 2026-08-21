"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        listMap = {}

        def copyList(node: 'Optional[Node]'):

            if not node:
                return

            if node in listMap:
                return listMap[node]

            newNode = Node(node.val)

            listMap[node] = newNode
            newNode.next = copyList(node.next)
            newNode.random = copyList(node.random)

            return newNode

        copyList(head)

        if not head:
            return None

        return listMap[head]



