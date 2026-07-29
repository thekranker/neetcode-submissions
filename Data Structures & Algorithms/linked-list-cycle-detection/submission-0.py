# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        set = []
        currNode = head

        while currNode:
            if currNode in set:
                return True
            set.append(currNode)
            currNode = currNode.next
        
        return False
        