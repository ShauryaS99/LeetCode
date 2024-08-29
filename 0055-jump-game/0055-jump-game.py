class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #O(n), greedy algo
        goalpost = len(nums) - 1
        
        # Move goalpost backwards
        for i in range(len(nums) - 1, -1, -1):
            # If we jump from our current position, can we reach goalpost or futher?
            if i + nums[i] >= goalpost:
                # Great! Then we move goalpost to that position
                goalpost = i
        
        if goalpost > 0:
            return False
        else:
            return True
            