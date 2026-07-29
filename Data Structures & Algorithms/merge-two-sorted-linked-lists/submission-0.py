# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 or list2:
        
            if list1 and not list2:
                newNode = ListNode(list1.val)
                tail.next = newNode
                tail = tail.next
                list1 = list1.next
            elif not list1 and list2:
                newNode = ListNode(list2.val)
                tail.next = newNode
                tail = tail.next
                list2 = list2.next
            elif list1.val <= list2.val:
                newNode = ListNode(list1.val)
                tail.next = newNode
                tail = tail.next
                list1 = list1.next
            elif list1.val > list2.val:
                newNode = ListNode(list2.val)
                tail.next = newNode
                tail = tail.next
                list2 = list2.next



        return dummy.next
        