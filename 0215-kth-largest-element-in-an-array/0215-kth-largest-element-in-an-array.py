import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Make values negative in accordance with min heap
        # O(nlogn)
        nums = [-1 * i for i in nums]
        hq.heapify(nums)
        ctr = 0
        res = 0
        while ctr < k:
            res = hq.heappop(nums)
            ctr += 1
        return -1 * res
        
        