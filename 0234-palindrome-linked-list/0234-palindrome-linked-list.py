# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        stack = []
        while temp:
            stack.append(temp.val)
            temp = temp.next
        while head:
            if head.val == stack.pop():
                head = head.next
            else:
                return False
        return True