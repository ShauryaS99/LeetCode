class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) < 2:
            return 0
        while l <= r:
            mid = (l + r) // 2
            # Handle case when mid is on left edge
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    l = mid + 1
                    continue
            # Handle case when mid is on right edge
            elif mid == len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    r = mid - 1
                    continue
            # Found peak
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
                