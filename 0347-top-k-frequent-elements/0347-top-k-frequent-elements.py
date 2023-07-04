import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) - 1
        heap = []
        for key, value in freq.items():
            hq.heappush(heap, (value, key))
        res = []
        while len(res) < k:
            res.append(hq.heappop(heap)[1])
        return res
        