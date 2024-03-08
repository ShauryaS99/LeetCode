class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_counter = 0
        for i in nums:
            if i == 0:
                zero_counter += 1
        non_zero_pos = 0
        for i in nums:
            if i != 0:
                nums[non_zero_pos] = i
                non_zero_pos += 1
        for i in range(len(nums) - zero_counter, len(nums)):
            nums[i] = 0
        return nums
        