class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i in range(len(nums)):
            diff_dict[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_dict and i != diff_dict.get(diff):
                return [i, diff_dict.get(diff)]
            
        return [0,0]
        