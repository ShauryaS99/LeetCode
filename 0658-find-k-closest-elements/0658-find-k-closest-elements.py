import heapq as hq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #Heap approach O(nlogk) b/c heap is only size k
        res = []
        for i in range(k):
            hq.heappush(res, arr[i]) #push preliminary k items
        for i in range(k, len(arr)):
            if abs(x - arr[i]) < abs(x - res[0]): #only if distances is closer do we replace the elements
                hq.heappop(res)
                hq.heappush(res, arr[i])
        res.sort() #sort list 
        return res
            