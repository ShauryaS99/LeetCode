# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        temp = head
        curr = head.next
        while curr:
            temp.next = prev
            prev = temp
            temp = curr
            curr = curr.next
        temp.next = prev
        res = []
        # while temp:
        #     res.append(temp.val)
        #     temp = temp.next
        print(res)
        return temp

                
            
            
            