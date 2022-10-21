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
        
        def rotate(head):
            curr = head
            second_last = None
            while curr.next:
                if not curr.next.next:
                    second_last = curr
                curr = curr.next
            if second_last:
                second_last.next = None
            curr.next = head
            return curr
            
        while k > 0:
            head = rotate(head)
            k -= 1
        return head
