# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        fast = head
        while n > 0:
            fast = fast.next
            n -=1
        if not fast:
            return head.next
        
        slow = head
        prev = slow
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        
        return head
                
        