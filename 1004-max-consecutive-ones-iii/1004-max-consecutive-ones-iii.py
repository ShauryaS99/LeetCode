class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Find longest substr with max k 0's
        curr_ones = max_ones = 0
        l_idx = 0
        num_zero = 0
        # Move right ptr along
        for idx, r in enumerate(nums):
            if r == 0:
                num_zero += 1
            # While we exceed k 0's, shrink window
            while num_zero > k:
                if nums[l_idx] == 0:
                    num_zero -= 1
                l_idx += 1
            # Calculate curr substr
            max_ones = max(max_ones, idx - l_idx + 1)
            
        return max_ones