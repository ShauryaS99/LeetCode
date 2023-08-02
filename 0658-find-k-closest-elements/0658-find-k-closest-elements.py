import heapq as hq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #Binary tree approach b/c arr is already sorted: runs in O(logN)
        left, right = 0, len(arr) - k #keep len -k to have range
    
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x: #guarantee a spacing of k 
                left = mid + 1
            else:
                right = mid
        #left could be mid and mid: mid +k is the range 
        return arr[left:left + k]