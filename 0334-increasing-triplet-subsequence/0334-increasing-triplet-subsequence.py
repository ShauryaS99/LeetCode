class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        val_1 = float('inf')
        val_2 = float('inf')
        val_3 = float('inf')
        for i in range(len(nums)):
            if nums[i] <= val_1:
                val_1 = nums[i]
            elif nums[i] <= val_2:
                val_2 = nums[i]
            else:
                val_3 = nums[i]
                return True
        return False