# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n)
        if not head:
            return None
        
        prev = None
        curr = head
        while curr:
            temp = curr.next
            # Next ptr points to previous
            curr.next = prev
            # Update prev ptr
            prev = curr
            # Move to next node
            curr = temp
        
        return prev
            