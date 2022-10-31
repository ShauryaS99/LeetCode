# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        curr = head
        size = 0
        while curr:
            curr = curr.next
            size += 1
        
        dist_to_node = size - n
        if dist_to_node == 0:
            return head.next
        curr = head
        while curr:
            prev = curr
            curr = curr.next
            dist_to_node -= 1
            if dist_to_node == 0:
                prev.next = curr.next
        return head
                
        
