class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ptr_1 = 0
        ptr_2 = 0
        curr_sum = 0
        min_length = float('inf')
        while ptr_2 < len(nums):
            curr_sum += nums[ptr_2]
            while curr_sum >= target:
                min_length = min(min_length, ptr_2 - ptr_1 + 1)
                curr_sum -= nums[ptr_1]
                ptr_1 += 1
            ptr_2 += 1
        if min_length == float('inf'):
            return 0
        else:
            return min_length
            
            
            
        