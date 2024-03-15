class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_lst = [0] * len(nums)
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            sum_lst[i] = curr_sum
        return sum_lst
        