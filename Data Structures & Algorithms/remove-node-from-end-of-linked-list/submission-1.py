# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        firstPtr = dummy
        secondPtr = dummy

        for i in range(n):
            firstPtr = firstPtr.next

        # firstPtr is n steps ahead
        while firstPtr.next:
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next

        secondPtr.next = secondPtr.next.next

        return dummy.next
