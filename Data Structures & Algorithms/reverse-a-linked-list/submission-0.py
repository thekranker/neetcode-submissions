# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        # - Brainstorm - 
        # I need to reverse the linked list in O(n) TC and O(1) SC.
        # The first thing i'm noticing is that this appears to be a list, can't I just
        # iterate backwards and return that.
        # Could brute force it by storing all values in an array and the.n reversing it. This
        # would be O(n) time complexity and O(n) space complexity.
        # My idea right now is to change the self.nexts of each node and reverse it, then
        # I would return the list or something.
        # Got it, i'm going to use a prev variable and reverse the list as I iterate through
        # it.


        # empty list base case
        if head is None:
            return None

        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
            

        return prev

            





        

        