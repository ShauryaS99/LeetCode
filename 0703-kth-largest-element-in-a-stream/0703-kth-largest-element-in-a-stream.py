import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        hq.heapify(self.nums) #O(n)
        
        while len(self.nums) > k:
            hq.heappop(self.nums)

    def add(self, val: int) -> int:
        hq.heappush(self.nums, val) #add val but maintain heap value <= k
        if len(self.nums) > self.k:
            hq.heappop(self.nums)
        return self.nums[0]
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)