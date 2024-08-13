# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(nlogk)
        # Initialize heap with first values of k lists
        merged_heap = []
        for i in range(len(lists)):
            if lists[i]:
                hq.heappush(merged_heap, (lists[i].val, i))
        
        # Iteratively add K possible next nodes, and heappop the next one 
        curr = dummy = ListNode(0)
        while merged_heap:
            min_elem, curr_list = hq.heappop(merged_heap)
            # Set next to curr_lst, advance that list and add element to heap
            curr.next = lists[curr_list]
            curr = curr.next
            lists[curr_list] = lists[curr_list].next
            if curr.next:
                hq.heappush(merged_heap, (curr.next.val, curr_list))
        
        return dummy.next
            
        
        