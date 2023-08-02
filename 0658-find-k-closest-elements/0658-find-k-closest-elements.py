import heapq as hq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #Heap approach
        res = []
        for i in range(k):
            hq.heappush(res, arr[i])
        for i in range(k, len(arr)):
            if abs(x - arr[i]) < abs(x - res[0]):
                hq.heappop(res)
                hq.heappush(res, arr[i])
        res.sort()
        return res
            