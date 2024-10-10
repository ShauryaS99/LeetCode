class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        #O(n)
        nums = k
        for i in range(1, k + 1 + len(arr)):
            if i not in arr:
                nums -= 1
            if nums == 0:
                return i
        return -1
            