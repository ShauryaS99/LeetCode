class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(logN)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            mid_val = nums[mid]
            # Set mid, left, and right values
            if mid == 0:
                left_val = -float('inf')
            else:
                left_val = nums[mid - 1]
            if mid == len(nums) - 1:
                right_val = -float('inf')
            else:
                right_val = nums[mid + 1]
            # Do comparisons for binary search
            if left_val < mid_val and mid_val > right_val:
                return mid
            elif left_val < mid_val and mid_val < right_val:
                l = mid + 1
            else:
                r = mid - 1
