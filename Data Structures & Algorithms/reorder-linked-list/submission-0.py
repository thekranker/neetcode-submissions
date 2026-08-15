# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # first get a pointer that points to the middle of the list

        slowPtrPrev = None
        slowPtr = head
        fastPtr = head

        while fastPtr:
            slowPtrPrev = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
            if fastPtr:
                fastPtr = fastPtr.next

        slowPtrPrev.next = None
        # slowPtr is now in the middle of the list, fastPtr is at the end
        # reverse the list now from slowPtr -> end of list
        prev = None
        while slowPtr: 
            temp = slowPtr.next
            slowPtr.next = prev
            prev = slowPtr
            slowPtr = temp
        
        # with the second half of the list reversed,
        # merge the 2 lists together using fastPtr
        # 1 2 3
        # 4 5 6
        ptr = head
        second = prev
        while second:
            temp = ptr.next
            temp2 = second.next
            ptr.next = second
            second.next = temp
            ptr = temp
            second = temp2
            

    


