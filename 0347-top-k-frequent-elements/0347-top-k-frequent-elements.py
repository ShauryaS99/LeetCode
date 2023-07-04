import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # create frequency hashmap (unique keys)
        for i in nums:
            freq[i] = freq.get(i, 0) - 1 #keep frequencies as negative so easy use of minHeap
        heap = []
        for key, value in freq.items():
            hq.heappush(heap, (value, key)) #insert tuples of (frequency, key) so minheap can operate on frequency
        res = []
        while len(res) < k:
            res.append(hq.heappop(heap)[1]) #pop k values, we care about the key
        return res
        