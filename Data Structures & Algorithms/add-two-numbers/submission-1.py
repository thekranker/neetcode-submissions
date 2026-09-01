# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        newListDummy = ListNode(0, None)
        head = newListDummy
        carry = 0
        
        while l1 or l2 or carry:

            if l1 and not l2:
                head.next = ListNode((l1.val + carry) % 10, None)
                carry = (l1.val + carry) // 10
                l1 = l1.next
            elif l2 and not l1:
                head.next = ListNode((l2.val + carry) % 10, None)
                carry = (l2.val + carry) // 10
                l2 = l2.next
            elif l1 and l2:
                head.next = ListNode((l1.val + l2.val + carry) % 10, None)
                carry = (l1.val + l2.val + carry) // 10
                l1 = l1.next
                l2 = l2.next
            else:
                head.next = ListNode(carry, None)
                carry = 0
            head = head.next

        return newListDummy.next

