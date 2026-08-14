"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        clonedDict = {}

        def clone(node1: Optional['Node']) -> Optional['Node']:
            if not node1:
                return
            if node1 in clonedDict:
                return clonedDict[node1]

            clonedDict[node1] = Node(node1.val)
            for neighbor in node1.neighbors:
                clonedDict[node1].neighbors.append(clone(neighbor))
            
            return clonedDict[node1]

        return clone(node)
        
        
