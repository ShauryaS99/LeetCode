class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #O(logN)
        def binary_search(lst, start):        
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    if start:
                        if mid == 0 or nums[mid - 1] != target:
                            return mid
                        else:
                            r = mid - 1
                    else:
                        if mid == len(nums) - 1 or nums[mid + 1] != target:
                            return mid
                        else:
                            l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        start_idx = binary_search(nums, True)
        if start_idx == -1:
            return [-1, -1]
        end_idx = binary_search(nums, False)
        return [start_idx, end_idx]