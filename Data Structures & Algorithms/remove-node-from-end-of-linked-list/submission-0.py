# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        listLen = 1
        currHead = head
        dummy = ListNode(0, head)

        while currHead.next:
            listLen += 1
            currHead = currHead.next

        rmIndex = listLen - n
        currHead = dummy

        for i in range(rmIndex):
            currHead = currHead.next

        if currHead.next:
            currHead.next = currHead.next.next

        return dummy.next
