# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr1 = list1
        a_counter = 0
        b_counter = 0
        point_a = None
        point_b = None
        while curr1:
            # Next node needs to point to lst 2
            if a_counter == a - 1:
                point_a = curr1
            # Save pointer for end of lst 2 to point to
            if b_counter == b + 1:
                point_b = curr1
            a_counter += 1
            b_counter += 1
            curr1 = curr1.next
        curr2 = list2
        point_a.next = curr2
        # Get to end of list 2 to point to point_b
        while curr2:
            prev = curr2
            curr2 = curr2.next
        prev.next = point_b
        return list1