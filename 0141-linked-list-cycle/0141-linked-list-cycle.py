# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #O(n)
        if not head:
            return False
        
        slow = head
        fast = head.next
        while fast:
            if slow == fast:
                return True
            # If fast reaches the end: no cycle
            if not fast.next:
                return False
            # Update ptrs
            slow = slow.next
            fast = fast.next.next
        # Fast reached the end
        return False
        