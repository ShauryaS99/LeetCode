class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_subarray = 0
        num_deletions = 0
        l = 0
        #Dynamic sliding window
        for r, val in enumerate(nums):
            if val == 0:
                num_deletions += 1
            # Decrease window until we have 1 or fewer zeros
            while num_deletions > 1:
                if nums[l] == 0:
                    num_deletions -= 1
                l += 1
            # We subtract 1 from this formula b/c we MUST delete one element
            max_subarray = max(max_subarray, r - l + 1 - 1)
        return max_subarray