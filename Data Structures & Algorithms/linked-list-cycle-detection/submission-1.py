# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seenNodes = []
        currNode = head

        while currNode:
            if currNode in seenNodes:
                return True
            seenNodes.append(currNode)
            currNode = currNode.next
        
        return False
        