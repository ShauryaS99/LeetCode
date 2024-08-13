# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(nlogn)
        # Aggregate all linked lists into a min heap
        agg_lst = []
        for node in lists:
            while node:
                agg_lst.append(node.val)
                node = node.next
        hq.heapify(agg_lst)
        
        # Recreate linked list from min heap
        head = curr = ListNode(0)
        while agg_lst:
            elem = hq.heappop(agg_lst)
            curr.next = ListNode(elem)
            curr = curr.next
        
        return head.next
        