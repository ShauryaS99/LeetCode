import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(klogm) where m in unique elems in nums
        # Initialize frequency dict
        num_dict = {}
        for i in nums:
            num_dict[i] = num_dict.get(i, 0) + 1
        # Create heap of frequency tuples
        heap = []
        for num, freq in num_dict.items():
            heap.append((-1 * freq, num))
        hq.heapify(heap)
        # Get top k tuples
        res = []
        for i in range(k):
            freq, num = hq.heappop(heap)
            res.append(num)
        return res
        