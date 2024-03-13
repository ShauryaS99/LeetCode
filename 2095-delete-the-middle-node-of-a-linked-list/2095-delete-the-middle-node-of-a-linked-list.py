# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        if not fast:
            return None
        while fast:
            prev = slow
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
        prev.next = slow.next
        return head
        