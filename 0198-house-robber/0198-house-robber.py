class Solution:
    def rob(self, nums: List[int]) -> int:
        #Initialize a memoized list
        max_money = [0] * (len(nums))
        #Every iteration, take the max possible up until that point
        for i in range(len(nums)):
            if i == 0:
                max_money[i] = nums[i]
            elif i == 1:
                max_money[i] = max(nums[i], max_money[i - 1])
            else:
                #Either we keep the last max value, or we add curr value + 2 houses ago
                max_money[i] = max(nums[i] + max_money[i - 2], max_money[i - 1])
        return max_money[len(nums) - 1]