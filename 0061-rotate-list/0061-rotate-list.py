# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        def count_nodes(head):
            count = 1
            while head.next:
                head = head.next
                count += 1
            return count
        num_nodes = count_nodes(head)
        k = k % num_nodes
        if k == 0:
            return head
        
        def rotate(head, num_steps):
            curr = head
            new_head = head
            while curr.next:
                prev = curr
                curr = curr.next
                num_steps -= 1
                if num_steps == 0:
                    prev.next = None
                    new_head = curr
            curr.next = head
            return new_head
            
        num_steps = num_nodes - k
        new_head = rotate(head, num_steps)
        return new_head