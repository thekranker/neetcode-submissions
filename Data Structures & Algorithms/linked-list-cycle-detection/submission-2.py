# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slowPointer = head
        fastPointer = head

        while fastPointer:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
            if fastPointer:
                fastPointer = fastPointer.next
            if fastPointer and slowPointer == fastPointer:
                return True
        
        return False
        