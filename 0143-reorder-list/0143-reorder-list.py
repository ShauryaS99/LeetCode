# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Find middle of list (slow)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #Reverse 2nd half of list (prev)
        curr = slow
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        #Merge two lists
        curr = head
        while curr:
            nxt = curr.next #2
            curr.next = prev #1 > 4
            curr = nxt
            if prev:
                nxt = prev.next
                prev.next = curr
                prev = nxt
        return head
        
        