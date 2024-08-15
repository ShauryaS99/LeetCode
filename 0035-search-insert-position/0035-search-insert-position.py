class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(logN)
        l = 0
        r = len(nums) - 1
        # Binary Search
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        # If target less than mid > it will take its palce
        if nums[mid] > target:
            return mid
        # Else target is greater and it will come after
        else:
            return mid + 1
        