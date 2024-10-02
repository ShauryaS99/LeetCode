class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #O(nlogn + n^2)
        res = set()
        nums.sort()
        for idx, val in enumerate(nums):
            l = idx +1
            r = len(nums) - 1
            target = 0 - val
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.add((val, nums[l], nums[r]))
                    l += 1
                    r -= 1
        return res